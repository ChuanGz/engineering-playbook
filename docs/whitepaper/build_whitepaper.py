#!/usr/bin/env python3
"""Build the 25-page Engineering Playbook white paper."""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "engineering-decisions-that-hold-up-white-paper.pdf"
HERO = ROOT / "assets" / "decision-loop-hero.png"

W, H = A4
MM = 72 / 25.4
M = 18 * MM

NAVY = HexColor("#152238")
INK = HexColor("#1F2937")
CREAM = HexColor("#FFF8EE")
PAPER = HexColor("#FFFDF9")
CORAL = HexColor("#F4775C")
MINT = HexColor("#7CCDB5")
GOLD = HexColor("#F5BE62")
BLUE = HexColor("#6E8DD5")
SECONDARY = HexColor("#667085")
PALE_BLUE = HexColor("#E9EEF9")
PALE_MINT = HexColor("#E7F5F0")
PALE_CORAL = HexColor("#FDEAE5")
PALE_GOLD = HexColor("#FFF2D8")
WHITE = HexColor("#FFFFFF")


def register_fonts() -> None:
    font_dir = Path("/System/Library/Fonts/Supplemental")
    pdfmetrics.registerFont(TTFont("Arial", str(font_dir / "Arial.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Bold", str(font_dir / "Arial Bold.ttf")))
    pdfmetrics.registerFont(TTFont("Arial-Italic", str(font_dir / "Arial Italic.ttf")))
    pdfmetrics.registerFont(
        TTFont("Arial-BoldItalic", str(font_dir / "Arial Bold Italic.ttf"))
    )


def para(
    c: canvas.Canvas,
    text: str,
    x: float,
    y_top: float,
    width: float,
    size: float = 12,
    leading: float | None = None,
    color=INK,
    font: str = "Arial",
    align: int = TA_LEFT,
    max_height: float = 400,
) -> float:
    style = ParagraphStyle(
        "body",
        fontName=font,
        fontSize=size,
        leading=leading or size * 1.28,
        textColor=color,
        alignment=align,
        spaceAfter=0,
        spaceBefore=0,
    )
    p = Paragraph(text, style)
    _, ph = p.wrap(width, max_height)
    p.drawOn(c, x, y_top - ph)
    return ph


def label(c: canvas.Canvas, text: str, x: float, y: float, color=CORAL) -> None:
    c.setFillColor(color)
    c.setFont("Arial-Bold", 8.5)
    c.drawString(x, y, text.upper())


def page_title(
    c: canvas.Canvas,
    kicker: str,
    title: str,
    subtitle: str | None = None,
    dark: bool = False,
) -> float:
    fg = WHITE if dark else INK
    sub = HexColor("#CBD5E1") if dark else SECONDARY
    label(c, kicker, M, H - M, GOLD if dark else CORAL)
    title_h = para(
        c,
        title,
        M,
        H - M - 12,
        W - 2 * M,
        size=28,
        leading=31,
        color=fg,
        font="Arial-Bold",
    )
    y = H - M - 19 - title_h
    if subtitle:
        sub_h = para(c, subtitle, M, y, W - 2 * M, 11.5, 15, sub)
        y -= sub_h + 12
    return y


def footer(c: canvas.Canvas, page_no: int, source: str, dark: bool = False) -> None:
    color = HexColor("#AEB8C8") if dark else SECONDARY
    c.setStrokeColor(HexColor("#334155") if dark else HexColor("#E4E7EC"))
    c.setLineWidth(0.5)
    c.line(M, 14 * MM, W - M, 14 * MM)
    c.setFillColor(color)
    c.setFont("Arial", 7.2)
    c.drawString(M, 9.5 * MM, f"ENGINEERING DECISIONS THAT HOLD UP  •  SOURCE: {source}")
    c.setFont("Arial-Bold", 8)
    c.drawRightString(W - M, 9.5 * MM, f"{page_no:02d}")


def start(c: canvas.Canvas, bg=PAPER) -> None:
    c.setFillColor(bg)
    c.rect(0, 0, W, H, fill=1, stroke=0)


def end(c: canvas.Canvas, page_no: int, source: str, dark: bool = False) -> None:
    footer(c, page_no, source, dark)
    c.showPage()


def rounded(c, x, y, w, h, fill, radius=12, stroke=None, line_width=0.7):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke)
        c.setLineWidth(line_width)
        c.roundRect(x, y, w, h, radius, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, radius, fill=1, stroke=0)


def pill(c, text, x, y, fill=PALE_BLUE, fg=INK, width=None):
    c.setFont("Arial-Bold", 8.5)
    tw = pdfmetrics.stringWidth(text, "Arial-Bold", 8.5)
    width = width or tw + 16
    rounded(c, x, y, width, 21, fill, 10)
    c.setFillColor(fg)
    c.drawCentredString(x + width / 2, y + 7, text)


def icon(c, kind: str, cx: float, cy: float, color=INK, scale=1.0):
    c.saveState()
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(1.8 * scale)
    r = 11 * scale
    if kind == "target":
        c.circle(cx, cy, r, fill=0)
        c.circle(cx, cy, r * 0.55, fill=0)
        c.circle(cx, cy, r * 0.16, fill=1, stroke=0)
    elif kind == "evidence":
        c.roundRect(cx - r * .8, cy - r, r * 1.6, r * 2, 2, fill=0)
        for i, frac in enumerate((.45, .1, -.25)):
            c.line(cx - r * .45, cy + r * frac, cx + r * .45, cy + r * frac)
    elif kind == "options":
        c.line(cx - r, cy, cx + r, cy)
        c.line(cx, cy, cx, cy + r)
        c.circle(cx - r, cy, 2.3 * scale, fill=1, stroke=0)
        c.circle(cx + r, cy, 2.3 * scale, fill=1, stroke=0)
        c.circle(cx, cy + r, 2.3 * scale, fill=1, stroke=0)
    elif kind == "decision":
        c.line(cx - r, cy, cx - r * .2, cy - r * .7)
        c.line(cx - r * .2, cy - r * .7, cx + r, cy + r * .7)
    elif kind == "delivery":
        c.rect(cx - r, cy - r * .65, r * 2, r * 1.3, fill=0)
        c.line(cx - r, cy, cx + r, cy)
        c.line(cx, cy, cx, cy + r * .65)
    elif kind == "feedback":
        c.arc(cx-r, cy-r, cx+r, cy+r, 35, 250)
        c.line(cx + r * .75, cy - r * .15, cx + r * .9, cy - r * .65)
        c.line(cx + r * .9, cy - r * .65, cx + r * .4, cy - r * .55)
    elif kind == "learn":
        c.circle(cx, cy + r * .2, r * .72, fill=0)
        c.line(cx - r * .35, cy - r * .55, cx - r * .35, cy - r)
        c.line(cx + r * .35, cy - r * .55, cx + r * .35, cy - r)
        c.line(cx - r * .35, cy - r, cx + r * .35, cy - r)
    elif kind == "shield":
        p = c.beginPath()
        p.moveTo(cx, cy + r)
        p.lineTo(cx + r * .8, cy + r * .55)
        p.lineTo(cx + r * .62, cy - r * .55)
        p.lineTo(cx, cy - r)
        p.lineTo(cx - r * .62, cy - r * .55)
        p.lineTo(cx - r * .8, cy + r * .55)
        p.close()
        c.drawPath(p, fill=0)
    elif kind == "people":
        c.circle(cx - r * .45, cy + r * .35, r * .25, fill=0)
        c.circle(cx + r * .45, cy + r * .35, r * .25, fill=0)
        c.arc(cx-r, cy-r, cx, cy+r*.2, 5, 170)
        c.arc(cx, cy-r, cx+r, cy+r*.2, 5, 170)
    elif kind == "book":
        c.roundRect(cx - r, cy - r * .8, r * .9, r * 1.6, 2, fill=0)
        c.roundRect(cx + r * .1, cy - r * .8, r * .9, r * 1.6, 2, fill=0)
        c.line(cx, cy - r * .8, cx, cy + r * .8)
    elif kind == "clock":
        c.circle(cx, cy, r, fill=0)
        c.line(cx, cy, cx, cy + r * .55)
        c.line(cx, cy, cx + r * .45, cy - r * .25)
    c.restoreState()


def arrow(c, x1, y1, x2, y2, color=SECONDARY, width=1.3, head=5):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    c.line(x1, y1, x2, y2)
    angle = math.atan2(y2 - y1, x2 - x1)
    for delta in (2.55, -2.55):
        c.line(
            x2,
            y2,
            x2 + head * math.cos(angle + delta),
            y2 + head * math.sin(angle + delta),
        )


def card(c, x, y, w, h, title, body, accent=CORAL, num=None, dark=False):
    fill = HexColor("#20304A") if dark else WHITE
    fg = WHITE if dark else INK
    body_color = HexColor("#CBD5E1") if dark else SECONDARY
    rounded(c, x, y, w, h, fill, 12, HexColor("#334155") if dark else HexColor("#E6E9EE"))
    c.setFillColor(accent)
    c.roundRect(x, y + h - 6, w, 6, 3, fill=1, stroke=0)
    tx = x + 14
    if num is not None:
        c.setFillColor(accent)
        c.setFont("Arial-Bold", 22)
        c.drawString(tx, y + h - 35, str(num))
        title_top = y + h - 45
    else:
        title_top = y + h - 20
    th = para(c, title, tx, title_top, w - 28, 11.5, 14, fg, "Arial-Bold")
    para(c, body, tx, title_top - th - 7, w - 28, 9.1, 12, body_color)


def draw_fit_image(c, path, x, y, w, h):
    image = Image.open(path)
    iw, ih = image.size
    scale = max(w / iw, h / ih)
    sw, sh = w / scale, h / scale
    left = (iw - sw) / 2
    top = (ih - sh) / 2
    cropped = image.crop((left, top, left + sw, top + sh))
    c.drawImage(ImageReader(cropped), x, y, w, h, mask="auto")


def page_01(c):
    start(c, CREAM)
    draw_fit_image(c, HERO, 0, H * .37, W, H * .63)
    c.setFillColor(NAVY)
    c.rect(0, 0, W, H * .39, fill=1, stroke=0)
    label(c, "Engineering Playbook White Paper", M, H * .335, GOLD)
    para(c, "Engineering<br/>decisions<br/>that hold up", M, H * .305, W - 2 * M, 31, 33, WHITE, "Arial-Bold")
    para(c, "A practical operating model for moving from unclear problems to safe delivery—and back to learning.", M, 81, W - 2 * M, 11.5, 15, HexColor("#D9E2EE"))
    c.setFillColor(MINT)
    c.rect(M, 59, 42, 3.5, fill=1, stroke=0)
    c.setFillColor(HexColor("#AEB8C8"))
    c.setFont("Arial", 7.5)
    c.drawString(M, 42, "ENGINEERING PLAYBOOK  •  WHITE PAPER  •  JUNE 2026")
    c.showPage()


def page_02(c):
    start(c)
    y = page_title(c, "Executive premise", "Good engineering is a chain of reviewable decisions.", "Tools, frameworks, and ceremonies help only when they preserve the reasoning that connects consequence to evidence.")
    metrics = [
        ("9", "engineering domains", "One authoritative home for each kind of decision."),
        ("60", "domain sources", "Guides and indexes that expose trade-offs and failure modes."),
        ("10", "working templates", "Small artifacts for reviews, risks, estimates, and learning."),
        ("7", "content standards", "Rules that reject filler, invented evidence, and empty process."),
    ]
    gap = 12
    cw = (W - 2 * M - gap) / 2
    ch = 112
    for i, (n, t, b) in enumerate(metrics):
        col, row = i % 2, i // 2
        x = M + col * (cw + gap)
        yy = y - 7 - (row + 1) * ch - row * 12
        rounded(c, x, yy, cw, ch, [PALE_CORAL, PALE_MINT, PALE_GOLD, PALE_BLUE][i], 14)
        c.setFont("Arial-Bold", 30)
        c.setFillColor([CORAL, MINT, GOLD, BLUE][i])
        c.drawString(x + 15, yy + 66, n)
        para(c, t, x + 15, yy + 61, cw - 30, 11, 13, INK, "Arial-Bold")
        para(c, b, x + 15, yy + 40, cw - 30, 8.7, 11, SECONDARY)
    rounded(c, M, 85, W - 2 * M, 66, NAVY, 13)
    para(c, "The promise is deliberately modest: make the next consequential decision easier to understand, challenge, verify, and revise.", M + 18, 131, W - 2 * M - 36, 12.5, 16, WHITE, "Arial-Bold")
    end(c, 2, "README.md; docs/README.md; repository file inventory")


def page_03(c):
    start(c, NAVY)
    y = page_title(c, "The stable core", "One loop. Seven decisions. No theater.", "Every practice in the playbook should help the work move forward or strengthen the evidence around it.", True)
    names = [
        ("Problem", "target", CORAL), ("Evidence", "evidence", MINT),
        ("Options", "options", GOLD), ("Decision", "decision", BLUE),
        ("Delivery", "delivery", CORAL), ("Feedback", "feedback", MINT),
        ("Learning", "learn", GOLD),
    ]
    center_x, center_y = W / 2, 365
    radius = 177
    positions = []
    for i, (name, kind, col) in enumerate(names):
        angle = math.radians(115 - i * 360 / 7)
        x, yy = center_x + radius * math.cos(angle), center_y + radius * math.sin(angle)
        positions.append((x, yy))
        c.setFillColor(HexColor("#20304A"))
        c.circle(x, yy, 31, fill=1, stroke=0)
        icon(c, kind, x, yy + 4, col, .75)
        c.setFillColor(WHITE)
        c.setFont("Arial-Bold", 8.5)
        c.drawCentredString(x, yy - 20, name)
    for i in range(len(positions)):
        x1, y1 = positions[i]
        x2, y2 = positions[(i + 1) % len(positions)]
        dx, dy = x2 - x1, y2 - y1
        dist = math.hypot(dx, dy)
        arrow(c, x1 + dx / dist * 35, y1 + dy / dist * 35, x2 - dx / dist * 35, y2 - dy / dist * 35, HexColor("#66758C"), 1.1, 4)
    rounded(c, center_x - 76, center_y - 36, 152, 72, CREAM, 14)
    para(c, "Use the smallest practice that protects a named outcome.", center_x - 61, center_y + 17, 122, 12.5, 16, NAVY, "Arial-Bold", TA_CENTER)
    end(c, 3, "README.md — The decision-to-learning loop", True)


def page_04(c):
    start(c)
    y = page_title(c, "Proportional rigor", "Rigor follows consequence—not habit.", "The smallest useful control changes as impact, uncertainty, and reversibility change.")
    x0, y0, mw, mh = M + 18, 205, W - 2 * M - 36, 330
    c.setFillColor(PALE_BLUE)
    c.roundRect(x0, y0, mw, mh, 14, fill=1, stroke=0)
    cols = ["Low", "Medium", "High"]
    rows = ["Reversible", "Costly to reverse", "Irreversible effects"]
    cell_w, cell_h = mw / 3, mh / 3
    fills = [[PALE_MINT, PALE_MINT, PALE_GOLD], [PALE_MINT, PALE_GOLD, PALE_CORAL], [PALE_GOLD, PALE_CORAL, CORAL]]
    texts = [["Reuse evidence", "Targeted check", "Focused review"], ["Focused review", "Recorded decision", "Staged exposure"], ["Recovery proof", "Staged exposure", "Strongest control"]]
    for r in range(3):
        for col in range(3):
            x, yy = x0 + col * cell_w, y0 + (2-r) * cell_h
            c.setFillColor(fills[r][col])
            c.rect(x + 2, yy + 2, cell_w - 4, cell_h - 4, fill=1, stroke=0)
            para(c, texts[r][col], x + 9, yy + cell_h/2 + 8, cell_w - 18, 9.5, 12, NAVY if fills[r][col] != CORAL else WHITE, "Arial-Bold", TA_CENTER)
    c.saveState(); c.translate(M - 5, y0 + mh/2); c.rotate(90)
    c.setFont("Arial-Bold", 8); c.setFillColor(SECONDARY); c.drawCentredString(0, 0, "REVERSIBILITY")
    c.restoreState()
    c.setFont("Arial-Bold", 8); c.setFillColor(SECONDARY); c.drawCentredString(x0 + mw/2, y0 - 18, "IMPACT + UNCERTAINTY")
    for i, t in enumerate(cols):
        c.setFont("Arial-Bold", 8); c.setFillColor(SECONDARY); c.drawCentredString(x0 + cell_w*(i+.5), y0 + mh + 10, t.upper())
    for i, t in enumerate(rows):
        c.setFillColor(SECONDARY); c.setFont("Arial", 7.5); c.drawRightString(x0 - 8, y0 + mh - cell_h*(i+.5) - 2, t)
    rounded(c, M, 102, W - 2*M, 62, NAVY, 12)
    para(c, "A low-consequence change should not carry enterprise ceremony. A one-line permission change may deserve the strongest evidence in the room.", M+16, 143, W-2*M-32, 11.2, 15, WHITE, "Arial-Bold")
    end(c, 4, "README.md; docs/delivery/delivery-risk.md")


def page_05(c):
    start(c, CREAM)
    y = page_title(c, "Workflow-neutral", "Start at the decision. Ceremonies are only coordinates.", "Scrum, Kanban, hybrid, and continuous flow can surface the same engineering question.")
    stages = ["Frame", "Clarify", "Slice", "Decide", "Build + verify", "Release", "Observe", "Learn"]
    x = M
    yy = y - 75
    total_w = W - 2*M
    gap = 5
    sw = (total_w - gap*3)/4
    for i, s in enumerate(stages):
        row, col = i//4, i%4
        xx = x + col*(sw+gap)
        sy = yy - row*77
        rounded(c, xx, sy, sw, 51, [PALE_CORAL, PALE_MINT, PALE_GOLD, PALE_BLUE][col], 10)
        c.setFillColor([CORAL, MINT, GOLD, BLUE][col]); c.setFont("Arial-Bold", 16)
        c.drawString(xx+10, sy+27, f"{i+1}")
        para(c, s, xx+10, sy+22, sw-20, 8.8, 10.5, INK, "Arial-Bold")
        if i < 7:
            nx = x + ((i+1)%4)*(sw+gap) if (i+1)%4 else x
            ny = yy - ((i+1)//4)*77 + 25
            if i != 3:
                arrow(c, xx+sw, sy+25, xx+sw+gap-1, sy+25, SECONDARY, .9, 3)
    bands = [
        ("Scrum", "refinement • planning • daily delivery • review • retrospective", CORAL),
        ("Kanban", "replenishment • explicit policy • WIP flow • service review", MINT),
        ("Hybrid", "useful touchpoints • explicit owner • observable evidence", BLUE),
    ]
    by = 280
    for i,(name,body,col) in enumerate(bands):
        rounded(c, M, by-i*67, W-2*M, 52, WHITE, 10, HexColor("#E6E0D8"))
        c.setFillColor(col); c.rect(M, by-i*67, 7, 52, fill=1, stroke=0)
        para(c, name, M+18, by-i*67+37, 75, 10, 12, INK, "Arial-Bold")
        para(c, body, M+95, by-i*67+36, W-2*M-112, 9.2, 12, SECONDARY)
    para(c, "A ceremony is a place to decide—not proof that the decision is sound.", M, 112, W-2*M, 17, 21, NAVY, "Arial-Bold", TA_CENTER)
    end(c, 5, "docs/ways-of-working/delivery-flow.md")


def page_06(c):
    start(c)
    y = page_title(c, "Three practical journeys", "Slow down at the moments that can change the outcome.")
    items = [
        ("01", "Unclear idea", "Clarify the outcome, expose ambiguity, validate the riskiest assumption, and shape one testable slice.", "Testable slice", CORAL, "target"),
        ("02", "Risky change", "Compare options, review failure paths, map risk to evidence, and prove recovery before exposure.", "Safe release decision", BLUE, "shield"),
        ("03", "Poor outcome", "Separate observation from explanation, examine system conditions, and run one owned experiment.", "Learning experiment", MINT, "learn"),
    ]
    cy = y - 25
    for i,(n,t,b,out,col,kind) in enumerate(items):
        h=139; yy=cy-(i+1)*h-i*15
        rounded(c,M,yy,W-2*M,h,[PALE_CORAL,PALE_BLUE,PALE_MINT][i],14)
        c.setFillColor(col); c.setFont("Arial-Bold",28); c.drawString(M+18,yy+h-40,n)
        icon(c,kind,W-M-38,yy+h-38,col,1.05)
        para(c,t,M+18,yy+h-51,W-2*M-80,15,18,INK,"Arial-Bold")
        para(c,b,M+18,yy+h-82,W-2*M-36,9.5,12.5,SECONDARY)
        pill(c,out,M+18,yy+16,[WHITE,WHITE,WHITE][i],col)
    end(c,6,"docs/ways-of-working/README.md")


def page_07(c):
    start(c, NAVY)
    y = page_title(c, "Problem framing", "Keep the solution outside the frame—until evidence earns it a seat.", None, True)
    inputs = [("Required outcome",CORAL),("Fixed constraints",MINT),("Quality scenarios",GOLD),("Material unknowns",BLUE)]
    fx, fy, fw, fh = W/2-78, 315, 156, 112
    for i,(t,col) in enumerate(inputs):
        yy=535-i*67
        rounded(c,M,yy,153,47,HexColor("#20304A"),10,HexColor("#334155"))
        c.setFillColor(col); c.circle(M+18,yy+23.5,5,fill=1,stroke=0)
        para(c,t,M+31,yy+31,112,9.2,11,WHITE,"Arial-Bold")
        arrow(c,M+153,yy+23.5,fx,fy+fh/2,HexColor("#6B7B91"),1,4)
    rounded(c,fx,fy,fw,fh,CREAM,16)
    para(c,"PROBLEM<br/>FRAME",fx+18,fy+78,fw-36,21,22,NAVY,"Arial-Bold",TA_CENTER)
    arrow(c,fx+fw,fy+fh*.66,W-M-120,fy+fh*.66,MINT,1.5,5)
    arrow(c,fx+fw,fy+fh*.34,W-M-120,fy+fh*.34,GOLD,1.5,5)
    para(c,"Next design<br/>decision",W-M-112,fy+fh*.78,110,10.5,13,WHITE,"Arial-Bold",TA_CENTER)
    para(c,"Validation<br/>needed",W-M-112,fy+fh*.46,110,10.5,13,WHITE,"Arial-Bold",TA_CENTER)
    rounded(c,M,155,W-2*M,78,HexColor("#20304A"),12,HexColor("#334155"))
    para(c,"“Highly available” is not a quality scenario. Name the operation, failure condition, acceptable interruption, recovery target, and measurement source.",M+18,210,W-2*M-36,11.3,15,HexColor("#D9E2EE"),"Arial-Bold")
    pill(c,"Requested technology",M,112,PALE_CORAL,CORAL,138)
    c.setFillColor(HexColor("#AEB8C8")); c.setFont("Arial-Italic",8.5); c.drawString(M+149,119,"stays outside unless it is a proven fixed constraint")
    end(c,7,"docs/system-design/problem-framing.md",True)


def page_08(c):
    start(c)
    y = page_title(c, "Ambiguity", "Vague words are tiny forks in the road.", "Expose the fork before two reasonable teams build two different truths.")
    vague=["fast","simple","secure","real time","large","as needed"]
    xx=M
    for i,v in enumerate(vague):
        w=62 if i!=3 else 76
        pill(c,v,xx,y-54,[PALE_CORAL,PALE_GOLD,PALE_MINT,PALE_BLUE,PALE_GOLD,PALE_CORAL][i],[CORAL,GOLD,MINT,BLUE,GOLD,CORAL][i],w)
        xx+=w+7
    x1=M; x2=W/2+9; cw=W/2-M-18
    rounded(c,x1,350,cw,178,PALE_BLUE,14)
    rounded(c,x2,350,cw,178,PALE_MINT,14)
    label(c,"Interpretation A",x1+16,501,BLUE)
    para(c,"Status appears within one second—without refresh.",x1+16,480,cw-32,15,19,INK,"Arial-Bold")
    para(c,"This implies continuous delivery of updates, a latency target, and a failure state.",x1+16,420,cw-32,9.5,13,SECONDARY)
    label(c,"Interpretation B",x2+16,501,MINT)
    para(c,"Status appears on the next normal refresh.",x2+16,480,cw-32,15,19,INK,"Arial-Bold")
    para(c,"This may preserve a simpler request model and a different acceptance threshold.",x2+16,420,cw-32,9.5,13,SECONDARY)
    arrow(c,W/2,335,W/2,294,CORAL,1.5,6)
    rounded(c,M,188,W-2*M,94,NAVY,13)
    para(c,"Name the actor who can decide, then write the observable behavior that distinguishes the two paths.",M+20,255,W-2*M-40,13,17,WHITE,"Arial-Bold",TA_CENTER)
    para(c,"Precision helps only when it changes implementation, risk, or acceptance. Otherwise, label the uncertainty and move on.",M,139,W-2*M,10,14,SECONDARY,align=TA_CENTER)
    end(c,8,"docs/requirement-analysis/ambiguity-detection.md")


def page_09(c):
    start(c, CREAM)
    y=page_title(c,"Scope","Slice through the system—not across the org chart.","A useful slice produces an observable outcome or learning result.")
    half=(W-2*M-18)/2
    x1=M; x2=M+half+18
    rounded(c,x1,305,half,276,WHITE,14,HexColor("#E6E0D8"))
    label(c,"Component split",x1+16,552,CORAL)
    layers=[("Screen",PALE_CORAL,CORAL),("Service",PALE_GOLD,GOLD),("Database",PALE_BLUE,BLUE)]
    for i,(t,f,col) in enumerate(layers):
        yy=465-i*65
        rounded(c,x1+22,yy,half-44,47,f,9)
        para(c,t,x1+34,yy+31,half-68,10,12,INK,"Arial-Bold",TA_CENTER)
    para(c,"Activity completes. The user outcome is still waiting in pieces.",x1+20,345,half-40,9.5,13,SECONDARY,"Arial-Italic",TA_CENTER)
    rounded(c,x2,305,half,276,PALE_MINT,14)
    label(c,"Vertical slice",x2+16,552,MINT)
    icon(c,"people",x2+half/2,486,MINT,1.25)
    arrow(c,x2+half/2,454,x2+half/2,425,MINT,1.4,5)
    rounded(c,x2+22,369,half-44,52,NAVY,9)
    para(c,"Authorized user sees one known shipment status end to end.",x2+34,407,half-68,10,13,WHITE,"Arial-Bold",TA_CENTER)
    para(c,"One result. Clear exclusions. Independent acceptance.",x2+20,345,half-40,9.5,13,SECONDARY,"Arial-Italic",TA_CENTER)
    cards=[("Outcome","observable"),("Exclusions","explicit"),("Dependencies","justified")]
    gap=8; cw=(W-2*M-gap*2)/3
    for i,(a,b) in enumerate(cards):
        rounded(c,M+i*(cw+gap),190,cw,73,[PALE_CORAL,PALE_GOLD,PALE_BLUE][i],10)
        para(c,a,M+i*(cw+gap)+10,241,cw-20,9.5,11,INK,"Arial-Bold",TA_CENTER)
        para(c,b,M+i*(cw+gap)+10,218,cw-20,8.5,10,SECONDARY,align=TA_CENTER)
    para(c,"Keep slices large enough to create meaningful evidence—and small enough to change course.",M,135,W-2*M,12.5,16,NAVY,"Arial-Bold",TA_CENTER)
    end(c,9,"docs/requirement-analysis/scope-breakdown.md")


def page_10(c):
    start(c)
    y=page_title(c,"Validation","Test the assumption that can hurt the decision most.","Rank by consequence and weak evidence. Then choose the cheapest credible test.")
    mx,my,mw,mh=M+50,274,W-2*M-100,310
    c.setFillColor(PALE_BLUE); c.roundRect(mx,my,mw,mh,14,fill=1,stroke=0)
    c.setStrokeColor(WHITE); c.setLineWidth(2)
    c.line(mx+mw/2,my,mx+mw/2,my+mh); c.line(mx,my+mh/2,mx+mw,my+mh/2)
    quads=[
        ("Record it","Low impact / weak evidence",SECONDARY,mx,my+mh/2),
        ("Validate first","High impact / weak evidence",CORAL,mx+mw/2,my+mh/2),
        ("Proceed lightly","Low impact / strong evidence",MINT,mx,my),
        ("Protect the proof","High impact / strong evidence",BLUE,mx+mw/2,my),
    ]
    for title,body,col,x,yy in quads:
        para(c,title,x+14,yy+mh/2-22,mw/2-28,12,15,col,"Arial-Bold",TA_CENTER)
        para(c,body,x+14,yy+mh/2-55,mw/2-28,8.5,11,SECONDARY,align=TA_CENTER)
    c.saveState(); c.translate(M+15,my+mh/2); c.rotate(90); c.setFillColor(SECONDARY); c.setFont("Arial-Bold",8); c.drawCentredString(0,0,"IMPACT"); c.restoreState()
    c.setFillColor(SECONDARY); c.setFont("Arial-Bold",8); c.drawCentredString(mx+mw/2,my-18,"EVIDENCE STRENGTH")
    methods=["interview","existing data","workflow observation","prototype","technical spike","contract test"]
    xx=M
    for i,m in enumerate(methods):
        w=pdfmetrics.stringWidth(m,"Arial-Bold",8)+16
        if xx+w>W-M: xx=M; yline=188
        else: yline=217
        pill(c,m,xx,yline,[PALE_CORAL,PALE_GOLD,PALE_MINT,PALE_BLUE][i%4],[CORAL,GOLD,MINT,BLUE][i%4],w)
        xx+=w+6
    para(c,"Validation is useful only when it can change scope, acceptance, or the decision itself.",M,150,W-2*M,12.2,16,NAVY,"Arial-Bold",TA_CENTER)
    end(c,10,"docs/requirement-analysis/validation-before-implementation.md")


def page_11(c):
    start(c,NAVY)
    y=page_title(c,"Estimation","An estimate is a decision aid—not a promise wearing a number.",None,True)
    parts=[("Scope","what is included",CORAL),("Assumptions","what must remain true",MINT),("Unknowns","what may move the work",GOLD),("Range","how wide uncertainty is",BLUE),("Confidence","why the range deserves trust",CORAL),("Trigger","when to estimate again",MINT)]
    gap=12; cw=(W-2*M-gap)/2; ch=98
    for i,(t,b,col) in enumerate(parts):
        row,colidx=i//2,i%2; x=M+colidx*(cw+gap); yy=509-row*(ch+13)
        card(c,x,yy,cw,ch,t,b,col,num=i+1,dark=True)
    rounded(c,M,133,W-2*M,76,CREAM,13)
    para(c,"Use relative estimates to compare similar work. Use time ranges for capacity and commitments. Never convert points mechanically into dates.",M+18,185,W-2*M-36,11.2,15,NAVY,"Arial-Bold",TA_CENTER)
    end(c,11,"docs/requirement-analysis/estimation-strategy.md",True)


def page_12(c):
    start(c)
    y=page_title(c,"Design review","Trace behavior through success—and through the failure everyone hopes will not happen.")
    x0=M+15; x1=W-M-15; mid=W/2
    # Success lane
    label(c,"Critical success flow",M,548,MINT)
    nodes=[("Actor",M+30),("Boundary",M+135),("State",M+240),("Outcome",M+345)]
    for t,x in nodes:
        rounded(c,x,475,86,49,PALE_MINT,9)
        para(c,t,x+8,505,70,9.5,11,INK,"Arial-Bold",TA_CENTER)
    for i in range(3): arrow(c,nodes[i][1]+86,499,nodes[i+1][1]-3,499,MINT,1.3,5)
    # Failure lane
    label(c,"Material failure flow",M,421,CORAL)
    fnodes=[("Fault",M+30),("Signal",M+135),("Authority",M+240),("Recovery",M+345)]
    for t,x in fnodes:
        rounded(c,x,348,86,49,PALE_CORAL,9)
        para(c,t,x+8,378,70,9.5,11,INK,"Arial-Bold",TA_CENTER)
    for i in range(3): arrow(c,fnodes[i][1]+86,372,fnodes[i+1][1]-3,372,CORAL,1.3,5)
    checks=[("Drivers before components","The design exists to protect an outcome."),("Highest-impact assumptions","Challenge with evidence, not seniority."),("Simplest credible alternative","Complexity must earn its place."),("Disposition","Blocking, follow-up, accepted risk, or preference.")]
    gap=10; cw=(W-2*M-gap)/2
    for i,(t,b) in enumerate(checks):
        x=M+(i%2)*(cw+gap); yy=236-(i//2)*89
        rounded(c,x,yy,cw,75,[PALE_BLUE,PALE_GOLD,PALE_MINT,PALE_CORAL][i],10)
        para(c,t,x+12,yy+55,cw-24,9.7,12,INK,"Arial-Bold")
        para(c,b,x+12,yy+33,cw-24,8.3,10.5,SECONDARY)
    end(c,12,"docs/system-design/design-review.md")


def page_13(c):
    start(c,CREAM)
    y=page_title(c,"Trade-offs","A decision should show its scars.","Benefits are easy to present. Negative consequences, reversal cost, and reconsideration triggers make the choice reviewable.")
    steps=[("Drivers",CORAL),("Options",MINT),("Consequences",GOLD),("Assumptions",BLUE),("Decision",CORAL),("Validation",MINT)]
    sx=M; sy=475; gap=8; sw=(W-2*M-gap*2)/3
    for i,(t,col) in enumerate(steps):
        row,colidx=i//3,i%3; x=sx+colidx*(sw+gap); yy=sy-row*94
        rounded(c,x,yy,sw,66,WHITE,10,HexColor("#E6E0D8"))
        c.setFillColor(col); c.circle(x+18,yy+45,6,fill=1,stroke=0)
        para(c,t,x+30,yy+51,sw-40,9.5,12,INK,"Arial-Bold")
        if i<5 and i!=2: arrow(c,x+sw,yy+33,x+sw+gap-1,yy+33,SECONDARY,.9,3)
    rounded(c,M,259,W-2*M,88,NAVY,13)
    para(c,"Compare at least two credible options—including the simplest current approach—under the same constraints.",M+18,321,W-2*M-36,13,17,WHITE,"Arial-Bold",TA_CENTER)
    left=M; bar_y=188
    para(c,"Weak decision",left,234,120,9,11,CORAL,"Arial-Bold")
    para(c,"“We chose X because it is scalable.”",left,214,W/2-M-18,10,13,SECONDARY,"Arial-Italic")
    para(c,"Reviewable decision",W/2+12,234,150,9,11,MINT,"Arial-Bold")
    para(c,"“X protects the top driver; we accept Y; evidence Z reopens the choice.”",W/2+12,214,W/2-M-12,10,13,SECONDARY,"Arial-Italic")
    para(c,"Scores may summarize reasoning. They cannot manufacture it.",M,132,W-2*M,13,17,NAVY,"Arial-Bold",TA_CENTER)
    end(c,13,"docs/system-design/trade-off-analysis.md")


def page_14(c):
    start(c)
    y=page_title(c,"Architecture boundaries","Put authority where change and invariants already travel together.")
    cx=W/2; cy=413
    circles=[(0,94,"Responsibility",CORAL),(112,-3,"State",MINT),(0,-101,"Contracts",GOLD),(-112,-3,"Change",BLUE)]
    for dx,dy,t,col in circles:
        c.setFillColor([PALE_CORAL,PALE_MINT,PALE_GOLD,PALE_BLUE][[CORAL,MINT,GOLD,BLUE].index(col)])
        c.circle(cx+dx,cy+dy,49,fill=1,stroke=0)
        para(c,t,cx+dx-39,cy+dy+6,78,10,12,INK,"Arial-Bold",TA_CENTER)
        arrow(c,cx+dx+(0 if dx==0 else (-35 if dx>0 else 35)),cy+dy+(35 if dy<0 else -35 if dy>0 else 0),cx,cy,col,1.1,4)
    rounded(c,cx-65,cy-39,130,78,NAVY,14)
    para(c,"ONE<br/>OWNER",cx-50,cy+20,100,17,18,WHITE,"Arial-Bold",TA_CENTER)
    rules=[("Keep invariants with state","Avoid routine cross-boundary transactions."),("Hide internal change","Consumers depend on contracts, not internals."),("Separate two decisions","Logical ownership does not require a network call.")]
    gap=9; cw=(W-2*M-gap*2)/3
    for i,(t,b) in enumerate(rules):
        rounded(c,M+i*(cw+gap),160,cw,108,[PALE_CORAL,PALE_MINT,PALE_BLUE][i],10)
        para(c,t,M+i*(cw+gap)+10,244,cw-20,9.5,12,INK,"Arial-Bold",TA_CENTER)
        para(c,b,M+i*(cw+gap)+10,205,cw-20,8.3,11,SECONDARY,align=TA_CENTER)
    para(c,"A neat diagram is not evidence for a deployment boundary.",M,128,W-2*M,12.5,16,NAVY,"Arial-Bold",TA_CENTER)
    end(c,14,"docs/architecture/boundaries.md")


def page_15(c):
    start(c,NAVY)
    y=page_title(c,"Implementation","Code should make the important truth hard to miss.",None,True)
    items=[
        ("Correctness visible","Keep invariants near the state they protect.",CORAL,"target"),
        ("Next reader first","Use names for responsibility and outcomes.",MINT,"people"),
        ("Side effects at boundaries","Separate decisions from I/O when it clarifies failure.",GOLD,"options"),
        ("Operational truth preserved","Bound timeouts; honor cancellation; expose meaningful state.",BLUE,"evidence"),
    ]
    gap=13; cw=(W-2*M-gap)/2; ch=176
    for i,(t,b,col,kind) in enumerate(items):
        row,colidx=i//2,i%2; x=M+colidx*(cw+gap); yy=392-row*(ch+14)
        rounded(c,x,yy,cw,ch,HexColor("#20304A"),14,HexColor("#334155"))
        c.setFillColor(col); c.circle(x+34,yy+ch-36,21,fill=0,stroke=1)
        icon(c,kind,x+34,yy+ch-36,col,.72)
        para(c,t,x+18,yy+ch-74,cw-36,13,16,WHITE,"Arial-Bold")
        para(c,b,x+18,yy+ch-118,cw-36,9.4,12.5,HexColor("#CBD5E1"))
    rounded(c,M,117,W-2*M,63,CREAM,12)
    para(c,"Abstraction earns its keep only when it protects a real variation, dependency, or invariant.",M+18,160,W-2*M-36,11.5,15,NAVY,"Arial-Bold",TA_CENTER)
    end(c,15,"docs/implementation/coding-principles.md",True)


def page_16(c):
    start(c)
    y=page_title(c,"Failure semantics","If every failure gets the same response, the categories are decorative.","Preserve enough meaning for callers to react and operators to recover.")
    failures=[
        ("Invalid input","correct",CORAL),("Business rejection","explain",GOLD),
        ("Concurrency conflict","refresh / retry",BLUE),("Dependency failure","bounded retry",MINT),
        ("Cancellation / deadline","stop cleanly",CORAL),("Unexpected defect","investigate",NAVY),
    ]
    gap=11; cw=(W-2*M-gap)/2; ch=88
    for i,(t,a,col) in enumerate(failures):
        row,colidx=i//2,i%2; x=M+colidx*(cw+gap); yy=496-row*(ch+12)
        rounded(c,x,yy,cw,ch,WHITE,11,HexColor("#E6E9EE"))
        c.setFillColor(col); c.rect(x,yy,7,ch,fill=1,stroke=0)
        para(c,t,x+18,yy+64,cw-36,10.5,13,INK,"Arial-Bold")
        pill(c,a,x+18,yy+17,[PALE_CORAL,PALE_GOLD,PALE_BLUE,PALE_MINT,PALE_CORAL,PALE_BLUE][i],col)
    rounded(c,M,139,W-2*M,78,NAVY,13)
    para(c,"Handle a failure only where context exists to recover, translate, or add useful evidence. Log once—at the accountable boundary.",M+18,194,W-2*M-36,11.3,15,WHITE,"Arial-Bold",TA_CENTER)
    end(c,16,"docs/implementation/error-handling.md")


def page_17(c):
    start(c,CREAM)
    y=page_title(c,"Test strategy","Test the risk—not the test framework.","Start from the harmful outcome, then buy the cheapest evidence that can reveal it.")
    risks=[("Violated invariant",CORAL),("Unsafe transition",GOLD),("Contract drift",BLUE),("Operational failure",MINT)]
    ev=[("unit behavior",PALE_CORAL),("integration boundary",PALE_GOLD),("contract evidence",PALE_BLUE),("canary + telemetry",PALE_MINT)]
    for i,((r,col),(e,fill)) in enumerate(zip(risks,ev)):
        yy=520-i*83
        rounded(c,M,yy,158,52,WHITE,10,HexColor("#E6E0D8"))
        c.setFillColor(col); c.circle(M+18,yy+26,5,fill=1,stroke=0)
        para(c,r,M+30,yy+33,116,9.2,11,INK,"Arial-Bold")
        arrow(c,M+158,yy+26,W-M-166,yy+26,SECONDARY,1.1,5)
        rounded(c,W-M-158,yy,158,52,fill,10)
        para(c,e,W-M-146,yy+33,134,9.2,11,INK,"Arial-Bold",TA_CENTER)
    rounded(c,M,155,W-2*M,73,NAVY,13)
    para(c,"Use the lowest sufficient boundary: include every component capable of causing the failure—then stop.",M+18,205,W-2*M-36,12,16,WHITE,"Arial-Bold",TA_CENTER)
    para(c,"Coverage is a map of executed code. It is not a map of protected consequences.",M,119,W-2*M,12.5,16,NAVY,"Arial-Bold",TA_CENTER)
    end(c,17,"docs/testing/testing-principles.md; docs/testing/test-strategy.md")


def page_18(c):
    start(c)
    y=page_title(c,"Code review","Review the consequence before the cosmetics.")
    pyramid=[
        ("Correctness • data • security • compatibility • recovery",CORAL,0),
        ("Design • boundaries • maintenance cost",GOLD,25),
        ("Evidence • tests • delivery controls",MINT,50),
        ("Style • formatting • preference",BLUE,75),
    ]
    base_y=318; total_w=W-2*M
    for i,(t,col,inset) in enumerate(pyramid):
        x=M+inset; w=total_w-2*inset; yy=base_y+i*67
        rounded(c,x,yy,w,51,[PALE_CORAL,PALE_GOLD,PALE_MINT,PALE_BLUE][i],10)
        para(c,t,x+12,yy+32,w-24,9.5,12,INK,"Arial-Bold",TA_CENTER)
    labels=[
        ("Finding","What can go wrong?"),("Consequence","Why does it matter?"),("Pass condition","What resolves it?"),("Owner","Who decides?"),
    ]
    gap=9; cw=(W-2*M-gap)/2
    for i,(t,b) in enumerate(labels):
        x=M+(i%2)*(cw+gap); yy=204-(i//2)*76
        rounded(c,x,yy,cw,63,WHITE,10,HexColor("#E6E9EE"))
        para(c,t,x+12,yy+43,82,9.5,11,[CORAL,GOLD,MINT,BLUE][i],"Arial-Bold")
        para(c,b,x+93,yy+43,cw-105,8.8,11,SECONDARY)
    end(c,18,"docs/code-review/review-principles.md")


def page_19(c):
    start(c,NAVY)
    y=page_title(c,"Delivery risk","A tiny diff can cast a very long shadow.",None,True)
    # Large 1 line visual
    c.setFillColor(CORAL); c.setFont("Arial-Bold",72); c.drawCentredString(W/2,494,"1")
    c.setFillColor(WHITE); c.setFont("Arial-Bold",13); c.drawCentredString(W/2,468,"LINE OF AUTHORIZATION LOGIC")
    c.setStrokeColor(HexColor("#52637A")); c.setLineWidth(1)
    c.line(M,438,W-M,438)
    risks=[("Blast radius","who can be harmed",CORAL),("Detectability","how quickly harm appears",GOLD),("Reversibility","what cannot be undone",MINT),("Authority","who can pause exposure",BLUE)]
    gap=11; cw=(W-2*M-gap)/2; ch=112
    for i,(t,b,col) in enumerate(risks):
        row,colidx=i//2,i%2; x=M+colidx*(cw+gap); yy=302-row*(ch+13)
        card(c,x,yy,cw,ch,t,b,col,dark=True)
    rounded(c,M,116,W-2*M,66,CREAM,12)
    para(c,"Risk follows impact, uncertainty, and low reversibility. Change size is not in the equation.",M+18,161,W-2*M-36,12,16,NAVY,"Arial-Bold",TA_CENTER)
    end(c,19,"docs/delivery/delivery-risk.md",True)


def page_20(c):
    start(c)
    y=page_title(c,"Release readiness","Four honest decisions beat one ceremonial green check.")
    decisions=[
        ("RELEASE","Evidence and recovery fit the impact.",MINT,PALE_MINT),
        ("STAGE","Uncertainty remains; exposure can be bounded.",BLUE,PALE_BLUE),
        ("HOLD","A critical outcome, control, or recovery path is unproven.",CORAL,PALE_CORAL),
        ("ACCEPT RISK","A bounded gap has an owner, monitoring, and expiry.",GOLD,PALE_GOLD),
    ]
    gap=12; cw=(W-2*M-gap)/2; ch=173
    for i,(t,b,col,fill) in enumerate(decisions):
        row,colidx=i//2,i%2; x=M+colidx*(cw+gap); yy=376-row*(ch+14)
        rounded(c,x,yy,cw,ch,fill,14)
        c.setFillColor(col); c.setFont("Arial-Bold",10); c.drawString(x+16,yy+ch-28,t)
        para(c,b,x+16,yy+ch-49,cw-32,13,17,INK,"Arial-Bold")
        c.setStrokeColor(col); c.setLineWidth(1.2); c.line(x+16,yy+25,x+cw-16,yy+25)
    rounded(c,M,114,W-2*M,60,NAVY,12)
    para(c,"Define success, stop, and recovery thresholds before the release date starts negotiating on your behalf.",M+16,155,W-2*M-32,10.8,14,WHITE,"Arial-Bold",TA_CENTER)
    end(c,20,"docs/delivery/release-readiness.md")


def page_21(c):
    start(c,CREAM)
    y=page_title(c,"Recovery","A previous artifact is not a rollback when state cannot move back.")
    # decision tree
    rounded(c,W/2-72,528,144,54,NAVY,11)
    para(c,"Harm detected",W/2-58,561,116,11,14,WHITE,"Arial-Bold",TA_CENTER)
    arrow(c,W/2,528,W/2,490,CORAL,1.4,5)
    rounded(c,W/2-95,434,190,56,PALE_GOLD,11)
    para(c,"All effects safely reversible?",W/2-78,469,156,10.5,13,INK,"Arial-Bold",TA_CENTER)
    arrow(c,W/2-95,462,M+105,388,MINT,1.3,5)
    arrow(c,W/2+95,462,W-M-105,388,CORAL,1.3,5)
    c.setFillColor(MINT); c.setFont("Arial-Bold",8); c.drawString(M+114,420,"YES")
    c.setFillColor(CORAL); c.drawRightString(W-M-114,420,"NO")
    rounded(c,M+28,330,154,58,PALE_MINT,11)
    para(c,"ROLLBACK",M+42,366,126,12,15,NAVY,"Arial-Bold",TA_CENTER)
    rounded(c,W-M-182,330,154,58,PALE_CORAL,11)
    para(c,"CONTAIN HARM",W-M-168,366,126,12,15,NAVY,"Arial-Bold",TA_CENTER)
    arrow(c,W-M-105,330,W-M-105,290,CORAL,1.3,5)
    options=[("Roll forward",CORAL),("Stabilize",GOLD),("Reconcile state",BLUE)]
    for i,(t,col) in enumerate(options):
        x=M+i*((W-2*M-16)/3+8); w=(W-2*M-16)/3
        rounded(c,x,209,w,58,[PALE_CORAL,PALE_GOLD,PALE_BLUE][i],10)
        para(c,t,x+9,245,w-18,9.5,12,INK,"Arial-Bold",TA_CENTER)
    rounded(c,M,118,W-2*M,63,NAVY,12)
    para(c,"Contain first when state is uncertain. Preserve evidence—but do not delay harm reduction for a perfect diagnosis.",M+16,161,W-2*M-32,10.7,14,WHITE,"Arial-Bold",TA_CENTER)
    end(c,21,"docs/delivery/rollback-and-recovery.md")


def page_22(c):
    start(c)
    y=page_title(c,"Documentation","Write for the action. Keep the truth near its owner.")
    principles=[
        ("Reader action","Name the task or decision the document enables.",CORAL,"people"),
        ("Truth near owner","Link volatile facts; do not copy them into drift.",MINT,"target"),
        ("One purpose","Separate learning, doing, lookup, and explanation.",GOLD,"book"),
        ("Deletion is maintenance","Supersede or remove content whose job has ended.",BLUE,"feedback"),
    ]
    for i,(t,b,col,kind) in enumerate(principles):
        yy=510-i*99
        rounded(c,M,yy,W-2*M,78,[PALE_CORAL,PALE_MINT,PALE_GOLD,PALE_BLUE][i],11)
        icon(c,kind,M+30,yy+39,col,.8)
        para(c,t,M+57,yy+55,145,10.5,13,INK,"Arial-Bold")
        para(c,b,M+206,yy+55,W-2*M-222,9.1,12,SECONDARY)
    rounded(c,M,125,W-2*M,70,NAVY,12)
    para(c,"Record decisions when reversal is expensive, ownership spans boundaries, or the same debate keeps returning. Preserve the original rationale when evidence later supersedes it.",M+16,176,W-2*M-32,10.5,14,WHITE,"Arial-Bold",TA_CENTER)
    end(c,22,"docs/documentation/documentation-principles.md; decision-records.md")


def page_23(c):
    start(c,NAVY)
    y=page_title(c,"Learning from outcomes","Blame ends inquiry. Evidence improves the system.",None,True)
    steps=[("Observed outcome",CORAL),("Available evidence",MINT),("System conditions",GOLD),("Small experiment",BLUE),("Review signal",CORAL)]
    sx=M; sy=492; gap=7; sw=(W-2*M-gap*4)/5
    for i,(t,col) in enumerate(steps):
        rounded(c,sx+i*(sw+gap),sy,sw,85,HexColor("#20304A"),10,HexColor("#334155"))
        c.setFillColor(col); c.setFont("Arial-Bold",18); c.drawCentredString(sx+i*(sw+gap)+sw/2,sy+55,str(i+1))
        para(c,t,sx+i*(sw+gap)+7,sy+39,sw-14,7.8,9.5,WHITE,"Arial-Bold",TA_CENTER)
        if i<4: arrow(c,sx+i*(sw+gap)+sw,sy+42,sx+(i+1)*(sw+gap)-1,sy+42,HexColor("#718198"),.9,3)
    dispositions=[("KEEP","benefit holds",MINT),("ADAPT","signal is promising",GOLD),("STOP","cost exceeds value",CORAL),("ESCALATE","authority sits elsewhere",BLUE)]
    gap=10; cw=(W-2*M-gap)/2; ch=93
    for i,(t,b,col) in enumerate(dispositions):
        row,colidx=i//2,i%2; x=M+colidx*(cw+gap); yy=342-row*(ch+12)
        rounded(c,x,yy,cw,ch,HexColor("#20304A"),11,HexColor("#334155"))
        para(c,t,x+14,yy+68,70,10,color=col,font="Arial-Bold")
        para(c,b,x+87,yy+68,cw-101,9.2,12,HexColor("#CBD5E1"))
    rounded(c,M,119,W-2*M,64,CREAM,12)
    para(c,"One owned experiment with a benefit signal, harm signal, and review trigger beats a long list of performative actions.",M+16,163,W-2*M-32,11,15,NAVY,"Arial-Bold",TA_CENTER)
    end(c,23,"docs/ways-of-working/learning-from-outcomes.md",True)


def page_24(c):
    start(c,CREAM)
    y=page_title(c,"Scaling","Scale the decision—not the ceremony.","Consistency belongs where consequences cross boundaries. Judgment stays close to the work.")
    layers=[
        ("Stable core","Durable principles, evidence standards, shared terminology.",NAVY,NAVY),
        ("Cross-boundary guardrails","Controls for shared safety, data, security, compliance, and compatibility.",CORAL,PALE_CORAL),
        ("Local adaptation","Team practices that preserve the shared contract without copying one workflow.",MINT,PALE_MINT),
        ("Evidence feedback","Outcomes and control cost can adapt—or remove—the rule.",BLUE,PALE_BLUE),
    ]
    widths=[W-2*M, W-2*M-46, W-2*M-92, W-2*M-138]
    top=535
    for i,(t,b,col,fill) in enumerate(layers):
        w=widths[i]; x=(W-w)/2; yy=top-i*105
        rounded(c,x,yy,w,82,fill,12)
        para(c,t,x+16,yy+59,w-32,11.5,14,WHITE if i==0 else INK,"Arial-Bold",TA_CENTER)
        para(c,b,x+16,yy+34,w-32,8.7,11,HexColor("#CBD5E1") if i==0 else SECONDARY,align=TA_CENTER)
    rules=["Name the cross-boundary harm.","Use the smallest shared guardrail.","Keep exceptions and removal triggers visible."]
    for i,r in enumerate(rules):
        c.setFillColor([CORAL,MINT,BLUE][i]); c.circle(M+9,142-i*23,4,fill=1,stroke=0)
        para(c,r,M+21,149-i*23,W-2*M-21,9.5,12,INK,"Arial-Bold")
    end(c,24,"docs/ways-of-working/scaling-without-bureaucracy.md")


def page_25(c):
    start(c,NAVY)
    y=page_title(c,"The short version","Build a system for better decisions—not a museum of process.",None,True)
    takeaways=[
        ("01","Start with consequence","Name the outcome, harmful failure, and owner before the preferred solution.",CORAL),
        ("02","Make evidence proportional","Increase rigor with impact, uncertainty, and low reversibility.",MINT),
        ("03","Keep trade-offs visible","A decision without negative consequences is an announcement.",GOLD),
        ("04","Design recovery early","Containment, authority, and state repair belong before release.",BLUE),
        ("05","Let learning remove rules","Experiments become policy only when evidence and ownership hold up.",CORAL),
    ]
    for i,(n,t,b,col) in enumerate(takeaways):
        yy=515-i*76
        rounded(c,M,yy,W-2*M,61,HexColor("#20304A"),11,HexColor("#334155"))
        c.setFillColor(col); c.setFont("Arial-Bold",17); c.drawString(M+15,yy+23,n)
        para(c,t,M+58,yy+42,150,10.5,13,WHITE,"Arial-Bold")
        para(c,b,M+214,yy+42,W-2*M-230,8.6,11,HexColor("#CBD5E1"))
    rounded(c,M,99,W-2*M,72,CREAM,13)
    para(c,"The playbook is working when the next decision becomes clearer, safer, and easier to revise—then gets out of the way.",M+18,150,W-2*M-36,12.5,16,NAVY,"Arial-Bold",TA_CENTER)
    c.setFillColor(HexColor("#91A0B5")); c.setFont("Arial",7.7)
    c.drawCentredString(W/2,78,"github.com/ChuanGz/engineering-playbook")
    c.linkURL("https://github.com/ChuanGz/engineering-playbook",(W/2-110,70,W/2+110,88),relative=0)
    end(c,25,"Engineering Playbook — durable takeaways",True)


def build() -> None:
    register_fonts()
    c = canvas.Canvas(str(OUTPUT), pagesize=A4, pageCompression=1)
    c.setTitle("Engineering Decisions That Hold Up")
    c.setSubject("A 25-page visual white paper based on the Engineering Playbook")
    c.setAuthor("Engineering Playbook contributors")
    c.setCreator("Engineering Playbook white paper builder")
    for fn in [
        page_01, page_02, page_03, page_04, page_05,
        page_06, page_07, page_08, page_09, page_10,
        page_11, page_12, page_13, page_14, page_15,
        page_16, page_17, page_18, page_19, page_20,
        page_21, page_22, page_23, page_24, page_25,
    ]:
        fn(c)
    c.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
