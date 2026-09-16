#!/usr/bin/env python3
"""Generate the synthetic, non-production walkthrough used by the README."""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
WIDTH, HEIGHT = 1200, 650


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


def gradient() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = image.load()
    top = (8, 20, 38)
    bottom = (11, 76, 79)
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        color = tuple(round(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        for x in range(WIDTH):
            pixels[x, y] = color
    return image


def rounded(draw: ImageDraw.ImageDraw, box, radius=18, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def multiline(draw, xy, text, size, fill, width, bold=False, spacing=7):
    draw.multiline_text(xy, text, font=font(size, bold), fill=fill, spacing=spacing, anchor=None)


def draw_route(draw, x, y, w, h):
    points = []
    for i in range(7):
        px = x + i * w / 6
        py = y + h * (0.52 + 0.22 * math.sin(i * 1.35))
        points.append((px, py))
    draw.line(points, fill=(14, 165, 164), width=7, joint="curve")
    for px, py in (points[0], points[-1]):
        draw.ellipse((px - 10, py - 10, px + 10, py + 10), fill=(245, 158, 11))


def draw_fake_qr(draw, x, y, size):
    rounded(draw, (x - 8, y - 8, x + size + 8, y + size + 8), 12, fill="white")
    rng = random.Random(20260915)
    cells = 13
    unit = size // cells
    for row in range(cells):
        for col in range(cells):
            if rng.random() > 0.56:
                draw.rectangle(
                    (x + col * unit, y + row * unit, x + (col + 1) * unit - 1, y + (row + 1) * unit - 1),
                    fill=(15, 23, 42),
                )
    draw.rectangle((x, y + size + 14, x + size, y + size + 45), fill=(226, 232, 240))
    draw.text((x + size / 2, y + size + 29), "QR DEMO", font=font(15, True), fill=(51, 65, 85), anchor="mm")


STEPS = [
    ("01", "Agendamento", "Janela, origem e destino\norganizados em um só lugar.", "schedule"),
    ("02", "Rota e lembretes", "Orientações claras antes e\ndurante o deslocamento.", "route"),
    ("03", "Documentos digitais", "Arquivos autorizados disponíveis\nna jornada correta.", "documents"),
    ("04", "Estoque em trânsito", "Eventos e recência ampliam a\nprevisibilidade operacional.", "transit"),
    ("05", "Check-in no pátio", "Chegada confirmada e espera\nsincronizada com o terminal.", "checkin"),
    ("06", "Chamada e QR Code", "Acesso liberado somente após\na autorização operacional.", "qr"),
    ("07", "Descarga iniciada", "Novo marco atualizado para\noperação e planejamento.", "unloading"),
]


def phone_shell(draw):
    x1, y1, x2, y2 = 760, 45, 1090, 605
    rounded(draw, (x1, y1, x2, y2), 42, fill=(8, 15, 30), outline=(148, 163, 184), width=3)
    rounded(draw, (x1 + 14, y1 + 14, x2 - 14, y2 - 14), 32, fill=(248, 250, 252))
    rounded(draw, (872, 57, 978, 76), 10, fill=(15, 23, 42))
    return x1 + 28, y1 + 92, x2 - 28, y2 - 34


def phone_header(draw, title, subtitle="Jornada DEMO-0001"):
    draw.text((790, 102), title, font=font(24, True), fill=(15, 23, 42))
    draw.text((790, 136), subtitle, font=font(14), fill=(100, 116, 139))
    draw.line((788, 166, 1062, 166), fill=(226, 232, 240), width=2)


def status_pill(draw, x, y, text, color=(13, 148, 136)):
    bbox = draw.textbbox((0, 0), text, font=font(13, True))
    w = bbox[2] - bbox[0] + 28
    rounded(draw, (x, y, x + w, y + 30), 15, fill=color)
    draw.text((x + w / 2, y + 15), text, font=font(13, True), fill="white", anchor="mm")


def draw_phone_content(draw, mode):
    if mode == "schedule":
        phone_header(draw, "Meu agendamento")
        status_pill(draw, 790, 188, "CONFIRMADO")
        draw.text((790, 236), "DD/MM · 14:00–15:00", font=font(23, True), fill=(15, 23, 42))
        rounded(draw, (790, 286, 1060, 385), 18, fill=(239, 246, 255))
        draw.text((810, 306), "ORIGEM A", font=font(13, True), fill=(3, 105, 161))
        draw.text((810, 337), "Pátio regulado → Terminal", font=font(17, True), fill=(30, 41, 59))
        draw.text((810, 365), "Operação: descarga", font=font(14), fill=(71, 85, 105))
        rounded(draw, (790, 430, 1060, 480), 16, fill=(13, 148, 136))
        draw.text((925, 455), "VER DETALHES", font=font(15, True), fill="white", anchor="mm")

    elif mode == "route":
        phone_header(draw, "Rota da operação")
        draw_route(draw, 800, 190, 245, 140)
        draw.text((790, 355), "Próximo destino", font=font(14), fill=(100, 116, 139))
        draw.text((790, 382), "Pátio regulado", font=font(23, True), fill=(15, 23, 42))
        rounded(draw, (790, 430, 1060, 505), 16, fill=(254, 243, 199))
        draw.text((808, 448), "LEMBRETE", font=font(12, True), fill=(161, 98, 7))
        draw.text((808, 474), "Chegue dentro da janela.", font=font(15, True), fill=(113, 63, 18))

    elif mode == "documents":
        phone_header(draw, "Documentos")
        for i, (name, state) in enumerate((("Documento fiscal", "DISPONÍVEL"), ("Liberação da carga", "VALIDADA"), ("Ordem operacional", "DISPONÍVEL"))):
            y = 194 + i * 96
            rounded(draw, (790, y, 1060, y + 76), 15, fill="white", outline=(203, 213, 225), width=2)
            rounded(draw, (806, y + 14, 846, y + 54), 9, fill=(224, 242, 254))
            draw.text((826, y + 34), "DOC", font=font(10, True), fill=(3, 105, 161), anchor="mm")
            draw.text((862, y + 15), name, font=font(15, True), fill=(30, 41, 59))
            draw.text((862, y + 43), state, font=font(11, True), fill=(13, 148, 136))
        draw.text((790, 510), "Dados e arquivos fictícios", font=font(12), fill=(148, 163, 184))

    elif mode == "transit":
        phone_header(draw, "Acompanhamento")
        status_pill(draw, 790, 188, "EM TRÂNSITO", (3, 105, 161))
        draw_route(draw, 800, 245, 245, 110)
        rounded(draw, (790, 390, 1060, 482), 16, fill=(236, 253, 245))
        draw.text((810, 407), "ÚLTIMO EVENTO", font=font(12, True), fill=(4, 120, 87))
        draw.text((810, 437), "Localização atualizada", font=font(17, True), fill=(6, 78, 59))
        draw.text((810, 464), "Sinal disponível · há poucos min", font=font(13), fill=(6, 95, 70))

    elif mode == "checkin":
        phone_header(draw, "Pátio regulado")
        rounded(draw, (790, 195, 1060, 338), 18, fill=(236, 253, 245), outline=(110, 231, 183), width=2)
        draw.ellipse((885, 215, 965, 295), fill=(13, 148, 136))
        draw.line((907, 257, 928, 278, 949, 238), fill="white", width=8, joint="curve")
        draw.text((925, 315), "CHECK-IN CONFIRMADO", font=font(15, True), fill=(6, 95, 70), anchor="mm")
        rounded(draw, (790, 375, 1060, 474), 16, fill=(241, 245, 249))
        draw.text((810, 394), "STATUS", font=font(12, True), fill=(100, 116, 139))
        draw.text((810, 423), "Aguardando chamada", font=font(19, True), fill=(30, 41, 59))
        draw.text((810, 450), "O QR ainda não está disponível.", font=font(13), fill=(71, 85, 105))

    elif mode == "qr":
        phone_header(draw, "Acesso ao terminal")
        status_pill(draw, 790, 182, "CHAMADA RECEBIDA", (217, 119, 6))
        draw_fake_qr(draw, 863, 240, 125)
        draw.text((925, 442), "Credencial temporária", font=font(15, True), fill=(30, 41, 59), anchor="mm")
        draw.text((925, 468), "Use apenas nesta jornada", font=font(13), fill=(100, 116, 139), anchor="mm")

    elif mode == "unloading":
        phone_header(draw, "Operação")
        rounded(draw, (790, 195, 1060, 350), 18, fill=(239, 246, 255), outline=(125, 211, 252), width=2)
        draw.ellipse((885, 220, 965, 300), fill=(3, 105, 161))
        draw.polygon(((910, 244), (945, 260), (910, 276)), fill="white")
        draw.text((925, 326), "DESCARGA INICIADA", font=font(16, True), fill=(7, 89, 133), anchor="mm")
        rounded(draw, (790, 388, 1060, 482), 16, fill=(236, 253, 245))
        draw.text((810, 407), "EVENTO SINCRONIZADO", font=font(12, True), fill=(4, 120, 87))
        draw.text((810, 438), "Planejamento atualizado", font=font(17, True), fill=(6, 78, 59))
        draw.text((810, 464), "Sem dados reais neste exemplo", font=font(13), fill=(6, 95, 70))


def make_frame(index: int, step) -> Image.Image:
    number, title, description, mode = step
    image = gradient()
    draw = ImageDraw.Draw(image)

    draw.ellipse((-160, -210, 390, 340), outline=(20, 184, 166), width=3)
    draw.ellipse((120, 420, 600, 900), outline=(14, 116, 144), width=2)
    draw.ellipse((1040, -130, 1390, 220), fill=(13, 148, 136))

    draw.text((70, 55), "CASE STUDY · DADOS FICTÍCIOS", font=font(15, True), fill=(94, 234, 212))
    draw.text((70, 105), "Jornada digital\ndo motorista", font=font(47, True), fill="white", spacing=2)
    draw.text((70, 240), number, font=font(76, True), fill=(245, 158, 11))
    draw.text((185, 250), title, font=font(31, True), fill="white")
    multiline(draw, (185, 298), description, 20, (203, 213, 225), 470, spacing=8)

    labels = ["Agenda", "Rota", "Docs", "Trânsito", "Pátio", "QR", "Descarga"]
    y = 500
    for i, label in enumerate(labels):
        x = 70 + i * 88
        active = i == index
        fill = (245, 158, 11) if active else (71, 85, 105)
        draw.ellipse((x, y, x + 18, y + 18), fill=fill)
        draw.text((x + 9, y + 35), label, font=font(11, active), fill=(255, 255, 255) if active else (148, 163, 184), anchor="mm")
        if i < len(labels) - 1:
            draw.line((x + 22, y + 9, x + 82, y + 9), fill=(71, 85, 105), width=3)

    draw.text((70, 600), "Reconstrução visual · sem telas ou informações do cliente", font=font(13), fill=(148, 163, 184))

    phone_shell(draw)
    draw_phone_content(draw, mode)
    return image


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    frames = [make_frame(i, step) for i, step in enumerate(STEPS)]
    frames[0].save(ASSETS / "demo-flow-preview.png", optimize=True)
    frames[0].save(
        ASSETS / "demo-flow.gif",
        save_all=True,
        append_images=frames[1:],
        duration=[1700] * len(frames),
        loop=0,
        optimize=True,
        disposal=2,
    )
    print(f"Generated {ASSETS / 'demo-flow.gif'}")


if __name__ == "__main__":
    main()
