import asyncio
from pyppeteer import launch


async def main1():
    import os
    myStr = str(os.getcwd())
    urlPath = 'file:///' + myStr + '/Templates/test2.html'
    pdf_path = "child/resultPDF.pdf"
    browser = await launch()
    page = await browser.newPage()
    await page.goto(urlPath)
    await page.pdf({'path': pdf_path, format: 'A4'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main1())
