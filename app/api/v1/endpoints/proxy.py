import re
from urllib.parse import parse_qs, urlparse

import httpx
from fastapi import APIRouter, HTTPException
from pathlib import Path
from fastapi.responses import HTMLResponse, Response, StreamingResponse
from starlette.background import BackgroundTask

router = APIRouter()


# ─────────────────────────────────────────────
# Utils
# ─────────────────────────────────────────────

def _extract_drive_file_id(url: str):
    patterns = [
        r"/file/d/([a-zA-Z0-9_-]+)",
        r"id=([a-zA-Z0-9_-]+)",
        r"/document/d/([a-zA-Z0-9_-]+)",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    try:
        parsed = urlparse(url)
        qs = parse_qs(parsed.query)
        if "id" in qs and qs["id"]:
            return qs["id"][0]
    except Exception:
        pass

    return None


def _normalize_pdf_url(url: str):
    if "drive.google.com" in url or "docs.google.com" in url:
        file_id = _extract_drive_file_id(url)
        if file_id:
            # 🔥 Evita redirect 303
            return f"https://drive.usercontent.google.com/download?id={file_id}&export=download"
    return url


def _is_drive_url(url: str):
    return "drive.google.com" in url or "usercontent.google.com" in url


# ─────────────────────────────────────────────
# Endpoints
# ─────────────────────────────────────────────

@router.get("/proxy/libro", response_class=HTMLResponse)
async def proxy_libro(url: str):
    final_url = _normalize_pdf_url(url)

    async with httpx.AsyncClient(follow_redirects=True, timeout=30) as client:
        res = await client.get(
            final_url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        content_type = res.headers.get("content-type", "").lower()

        # 🔥 Forzar PDF si viene de Drive
        if _is_drive_url(final_url):
            return Response(content=res.content, media_type="application/pdf")

        if "pdf" in content_type:
            return Response(content=res.content, media_type="application/pdf")

        return HTMLResponse(content=res.text)


@router.get("/proxy/pdf-viewer", response_class=HTMLResponse)
async def pdf_viewer():
    html_path = Path("app/static/pdfjs/pdf_viewer.html")
    return HTMLResponse(html_path.read_text(encoding="utf-8"))


@router.get("/proxy/pdf")
async def proxy_pdf(url: str):
    final_url = _normalize_pdf_url(url)

    client = httpx.AsyncClient(follow_redirects=True, timeout=120)

    request = client.build_request(
        "GET",
        final_url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    response = await client.send(request, stream=True)

    content_type = response.headers.get("content-type", "").lower()

    # 🔥 Forzar PDF para Drive
    if _is_drive_url(final_url):
        content_type = "application/pdf"

    # Si no es PDF, devolver tal cual
    if "pdf" not in content_type:
        body = await response.aread()
        await response.aclose()
        await client.aclose()

        return Response(
            content=body,
            media_type=response.headers.get("content-type", "application/octet-stream"),
            status_code=response.status_code
        )

    headers = {}
    if "content-length" in response.headers:
        headers["Content-Length"] = response.headers["content-length"]

    return StreamingResponse(
        response.aiter_bytes(),
        media_type="application/pdf",
        headers=headers,
        background=BackgroundTask(lambda: _close_response_and_client(response, client))
    )


async def _close_response_and_client(response, client):
    await response.aclose()
    await client.aclose()


@router.get("/proxy/portada")
async def proxy_portada(url: str):
    async with httpx.AsyncClient(follow_redirects=True, timeout=15) as client:
        res = await client.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        content_type = res.headers.get("content-type", "").lower()

        if res.status_code >= 400:
            raise HTTPException(
                status_code=res.status_code,
                detail="No se pudo obtener la portada"
            )

        if not content_type.startswith("image/"):
            raise HTTPException(
                status_code=404,
                detail="La portada no devolvió una imagen válida"
            )

        return Response(
            content=res.content,
            media_type=content_type,
            headers={
                "Cache-Control": "public, max-age=86400"
            }
        )