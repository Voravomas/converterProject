import asyncio
from pyppeteer import launch

async def main():
    pdf_path = "C:\\Users\\ura\\Desktop\\Курсач\\test1\\result.pdf"
    browser = await launch()
    page = await browser.newPage()
    await page.screenshot({'path': 'ple.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
