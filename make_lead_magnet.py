#!/usr/bin/env python3
"""Lead magnet: 'The 7 Business Models That Print Money' som designad PDF (mörk stil, guld)."""
import os
from PIL import Image, ImageDraw, ImageFont

FONTDIR = "/home/clawd/faceless-finance-shorts/fonts"
W, H = 1240, 1754          # A4 @150dpi
BG = (10, 14, 24)
GOLD = (255, 197, 61)
INK = (245, 247, 252)
GREY = (150, 160, 182)
RED = (255, 92, 92)
CARDBG = (20, 25, 40)

def F(weight, size):
    return ImageFont.truetype(os.path.join(FONTDIR, weight), size)

BLACK, XB, BOLD, SEMI, MED = "Inter-Black.ttf", "Inter-ExtraBold.ttf", "Inter-Bold.ttf", "Inter-SemiBold.ttf", "Inter-Medium.ttf"

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], []
    for w in words:
        t = " ".join(cur + [w])
        if d.textlength(t, font=font) <= maxw:
            cur.append(w)
        else:
            if cur: lines.append(" ".join(cur))
            cur = [w]
    if cur: lines.append(" ".join(cur))
    return lines

def page():
    return Image.new("RGB", (W, H), BG)

def footer(d, n):
    d.text((80, H - 90), "THE MARGIN", font=F(BOLD, 26), fill=GOLD)
    d.text((W - 80, H - 90), str(n), font=F(MED, 26), fill=GREY, anchor="ra")

def cover():
    img = page(); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 18], fill=GOLD)
    d.text((80, 200), "THE MARGIN", font=F(BLACK, 44), fill=GOLD)
    d.text((80, 270), "FREE BREAKDOWN", font=F(MED, 28), fill=GREY)
    y = 520
    for line in ["The 7", "Business Models", "That Print Money"]:
        d.text((80, y), line, font=F(BLACK, 118), fill=INK); y += 128
    d.text((80, y + 10), "…and the 3 that quietly kill good companies.", font=F(SEMI, 40), fill=GOLD)
    d.line([80, y + 110, W - 80, y + 110], fill=(60, 68, 90), width=3)
    d.text((80, y + 150), "Everything in this guide is what the world's biggest", font=F(MED, 34), fill=GREY)
    d.text((80, y + 195), "companies do — stripped to the principle you can copy.", font=F(MED, 34), fill=GREY)
    d.text((80, H - 200), "Built by The Margin", font=F(SEMI, 30), fill=INK)
    return img

MODELS = [
    ("01", "The Razor & Blades", GOLD,
     "Sell the handle cheap, get rich on the blades.",
     "The money is not in the first sale. It is in the repeat purchase you made unavoidable. "
     "Printers, coffee pods, razors, game consoles. The first product is a toll booth, not a product.",
     "Takeaway: design something the customer must keep buying, then price the entry low.",
     "Watch out: if the refill is commoditised, the model collapses."),
    ("02", "The Landlord", GOLD,
     "Own the scarce asset, rent it out forever.",
     "McDonald's does not sell burgers. It buys the land, leases it to the franchisee, and takes the rent. "
     "With almost none of the operational risk. Rent is paid before anyone else earns a cent.",
     "Takeaway: find the scarce asset everyone needs, own it, and charge for access.",
     "Watch out: capital heavy — it only works at scale."),
    ("03", "The Platform", GOLD,
     "Let others do the work, take a cut of everything.",
     "Amazon's marketplace owns none of the sellers' inventory, yet takes a cut of every sale, plus fees, plus storage. "
     "You build the roads; everyone else pays the toll.",
     "Takeaway: build the marketplace, not the product. Charge for access, not inventory.",
     "Watch out: needs liquidity — no buyers means no sellers."),
    ("04", "The Subscription Flywheel", GOLD,
     "Recurring revenue turns loyalty into an annuity.",
     "Amazon Prime: you pay a yearly fee, so you shop more, so you get locked in, so you shop even more. "
     "Predictable revenue is worth far more than a one-off sale.",
     "Takeaway: convert one-off buyers into subscribers and let the loop compound.",
     "Watch out: churn kills it — retention is the whole game."),
    ("05", "The Infrastructure Play", GOLD,
     "Sell the picks and shovels, not the gold.",
     "During a gold rush, the people who get rich are the ones selling shovels. AWS — Amazon's cloud — quietly "
     "produces the majority of the company's profit. It sells the infrastructure everyone else is forced to rent.",
     "Takeaway: supply the tool everyone needs during a boom instead of competing in it.",
     "Watch out: extremely high margins attract ruthless competition."),
    ("06", "The Advertising Engine", GOLD,
     "Attention in, cash out.",
     "Google and Meta give away the product for free. You spend your time and data, and brands pay to interrupt you. "
     "Advertising is one of the highest-margin businesses ever built.",
     "Takeaway: if you own attention, you can monetise it without charging the user.",
     "Watch out: entirely dependent on holding the audience's attention."),
    ("07", "The Franchise", GOLD,
     "License the model instead of scaling it yourself.",
     "Instead of opening a thousand restaurants, McDonald's sells the right to use its name and system. "
     "Someone else funds the growth and carries the risk; you collect royalties.",
     "Takeaway: if you have a proven system, sell the system before you sell more units.",
     "Watch out: quality control — one bad franchisee damages the brand."),
]

FAILS = [
    ("A", "The One-Off Product", RED,
     "Every month starts at zero. No recurring revenue, no compounding — the treadmill never stops."),
    ("B", "The Race to the Bottom", RED,
     "Competing on price alone. Whoever is cheapest wins, and nobody makes money. Margin, not volume, is survival."),
    ("C", "Vanity Growth", RED,
     "Users, downloads, followers — and no profit. Growth that doesn't convert to cash is a hobby with a dashboard."),
]

def model_page(num, title, color, subtitle, body, take, warn, pageno):
    img = page(); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 14], fill=color)
    d.text((80, 120), num, font=F(BLACK, 150), fill=(45, 52, 72))
    d.text((80, 300), title, font=F(BLACK, 74), fill=INK)
    d.text((80, 400), subtitle, font=F(SEMI, 40), fill=color)
    y = 520
    for ln in wrap(d, body, F(MED, 38), W - 160):
        d.text((80, y), ln, font=F(MED, 38), fill=GREY); y += 56
    y += 40
    d.rounded_rectangle([70, y - 20, W - 70, y + 210], radius=24, fill=CARDBG)
    d.text((110, y + 10), "THE TAKEAWAY", font=F(BOLD, 30), fill=color)
    yy = y + 70
    for ln in wrap(d, take, F(SEMI, 38), W - 240):
        d.text((110, yy), ln, font=F(SEMI, 38), fill=INK); yy += 54
    y2 = y + 260
    d.text((80, y2), "Watch out:", font=F(BOLD, 34), fill=RED)
    yy = y2 + 54
    for ln in wrap(d, warn, F(MED, 34), W - 200):
        d.text((80, yy), ln, font=F(MED, 34), fill=GREY); yy += 48
    footer(d, pageno)
    return img

def fails_page(pageno):
    img = page(); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 14], fill=RED)
    d.text((80, 130), "The 3 that quietly", font=F(BLACK, 76), fill=INK)
    d.text((80, 220), "kill good companies.", font=F(BLACK, 76), fill=RED)
    y = 400
    for letter, title, color, body in FAILS:
        d.text((80, y), letter, font=F(BLACK, 60), fill=RED)
        d.text((160, y + 6), title, font=F(XB, 52), fill=INK)
        yy = y + 80
        for ln in wrap(d, body, F(MED, 34), W - 220):
            d.text((160, yy), ln, font=F(MED, 34), fill=GREY); yy += 48
        y = yy + 70
    footer(d, pageno)
    return img

def cta_page(pageno):
    img = page(); d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 18], fill=GOLD)
    d.text((80, 300), "Want the next one", font=F(BLACK, 84), fill=INK)
    d.text((80, 400), "before anyone else?", font=F(BLACK, 84), fill=GOLD)
    d.text((80, 560), "Every week I break down how another huge company", font=F(MED, 38), fill=GREY)
    d.text((80, 610), "really makes its money — the detail the press skips.", font=F(MED, 38), fill=GREY)
    y = 760
    for t in ["One company, one business model, 2 minutes.",
              "The principle behind it you can actually use.",
              "No hype. No fluff. Just the mechanics."]:
        d.ellipse([80, y + 12, 104, y + 36], fill=GOLD)
        d.text((130, y), t, font=F(SEMI, 36), fill=INK); y += 70
    d.rounded_rectangle([70, 1080, W - 70, 1240], radius=26, fill=CARDBG, outline=GOLD, width=3)
    d.text((W // 2, 1140), "SUBSCRIBE — IT'S FREE", font=F(BLACK, 52), fill=GOLD, anchor="mm")
    d.text((W // 2, 1200), "the-margin → newsletter", font=F(MED, 34), fill=GREY, anchor="mm")
    footer(d, pageno)
    return img

def main():
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lead-magnet.pdf")
    pages = [cover()]
    for i, m in enumerate(MODELS, 1):
        pages.append(model_page(*m, pageno=i + 1))
    pages.append(fails_page(pageno=9))
    pages.append(cta_page(pageno=10))
    pages[0].save(out, "PDF", resolution=150, save_all=True, append_images=pages[1:])
    print("KLAR:", out, len(pages), "sidor")

if __name__ == "__main__":
    main()
