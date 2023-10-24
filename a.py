from playwright.sync_api import sync_playwright

#play = sync_playwright().start()
#play.stop()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel='chrome', headless=False)
    page = browser.new_page(viewport={'width':1980,'height':2000})


    page.goto('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=논현동 날씨&tqi=igjO2sp0J14ssSoG7zZssssssTG-315332')

    weather_info = page.locator('div.content_wrap')
    weather_info.screenshot(path='info.png')