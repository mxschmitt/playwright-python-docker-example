# playwright-python-docker-example

This project is a demo about how to run playwright python inside Docker.

## Issue trying to reproduce

The problem I'm currently having with this project are two:

- [ ] Not able to run Playwright Python in headless mode.
- [ ] Not able to run Playwright Python with xvfb in headed mode.

### Steps for reproducing the issue

1. Build docker image:

```ssh
docker build -t example_playwright_python -f Dockerfile .
```

2. Run docker compose:

```
docker-compose up
```

3. The current output for running playwright in headless mode is the following

```
Creating network "playwright-python-docker-example_default" with the default driver
Creating playwright-python-docker-example_playwright_python_1 ... done
Attaching to playwright-python-docker-example_playwright_python_1
playwright_python_1  | ============================= test session starts ==============================
playwright_python_1  | platform linux -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0
playwright_python_1  | rootdir: /automation
playwright_python_1  | plugins: base-url-2.0.0, playwright-0.3.0
playwright_python_1  | collected 3 items
playwright_python_1  | 
playwright_python_1  | test_example.py .EE                                                      [100%]
playwright_python_1  | 
playwright_python_1  | ==================================== ERRORS ====================================
playwright_python_1  | _____________ ERROR at setup of test_example_with_context_fixture ______________
playwright_python_1  | 
playwright_python_1  |     @pytest.fixture()
playwright_python_1  |     def context():
playwright_python_1  |         with sync_playwright() as playwright:
playwright_python_1  | >           playwright_browser = playwright.chromium.launch(headless=True)
playwright_python_1  | 
playwright_python_1  | test_example.py:14: 
playwright_python_1  | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/sync_api/_generated.py:11690: in launch
playwright_python_1  |     self._sync(
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_browser_type.py:93: in launch
playwright_python_1  |     Browser, from_channel(await self._channel.send("launch", params))
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_connection.py:43: in send
playwright_python_1  |     return await self._connection.wrap_api_call(
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_connection.py:387: in wrap_api_call
playwright_python_1  |     return await cb()
playwright_python_1  | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
playwright_python_1  | 
playwright_python_1  | self = <playwright._impl._connection.Channel object at 0x7fba07209c10>
playwright_python_1  | method = 'launch', params = {'headless': True}, return_as_dict = False
playwright_python_1  | 
playwright_python_1  |     async def inner_send(
playwright_python_1  |         self, method: str, params: Optional[Dict], return_as_dict: bool
playwright_python_1  |     ) -> Any:
playwright_python_1  |         if params is None:
playwright_python_1  |             params = {}
playwright_python_1  |         callback = self._connection._send_message_to_server(self._guid, method, params)
playwright_python_1  |         if self._connection._error:
playwright_python_1  |             error = self._connection._error
playwright_python_1  |             self._connection._error = None
playwright_python_1  |             raise error
playwright_python_1  |         done, _ = await asyncio.wait(
playwright_python_1  |             {
playwright_python_1  |                 self._connection._transport.on_error_future,
playwright_python_1  |                 callback.future,
playwright_python_1  |             },
playwright_python_1  |             return_when=asyncio.FIRST_COMPLETED,
playwright_python_1  |         )
playwright_python_1  |         if not callback.future.done():
playwright_python_1  |             callback.future.cancel()
playwright_python_1  | >       result = next(iter(done)).result()
playwright_python_1  | E       playwright._impl._api_types.Error: 
playwright_python_1  | E       ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
playwright_python_1  | E       ║ Looks like you launched a headed browser without having a XServer running.                     ║
playwright_python_1  | E       ║ Set either 'headless: true' or use 'xvfb-run <your-playwright-app>' before running Playwright. ║
playwright_python_1  | E       ║                                                                                                ║
playwright_python_1  | E       ║ <3 Playwright Team                                                                             ║
playwright_python_1  | E       ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
playwright_python_1  | E       =========================== logs ===========================
playwright_python_1  | E       <launching> /ms-playwright/chromium-1019/chrome-linux/chrome --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-SGPIGb --remote-debugging-pipe --no-startup-window
playwright_python_1  | E       <launched> pid=113
playwright_python_1  | E       [pid=113][err] [113:113:0816/191913.971805:ERROR:ozone_platform_x11.cc(240)] Missing X server or $DISPLAY
playwright_python_1  | E       [pid=113][err] [113:113:0816/191913.972365:ERROR:env.cc(255)] The platform failed to initialize.  Exiting.
playwright_python_1  | E       ============================================================
playwright_python_1  | 
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_connection.py:78: Error
playwright_python_1  | ---------------------------- Captured stderr setup -----------------------------
playwright_python_1  | 2022-08-16T19:19:13.566Z pw:browser <launching> /ms-playwright/chromium-1019/chrome-linux/chrome --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-SGPIGb --remote-debugging-pipe --no-startup-window
playwright_python_1  | 2022-08-16T19:19:13.571Z pw:browser <launched> pid=113
playwright_python_1  | 2022-08-16T19:19:13.972Z pw:browser [pid=113][err] [113:113:0816/191913.971805:ERROR:ozone_platform_x11.cc(240)] Missing X server or $DISPLAY
playwright_python_1  | 2022-08-16T19:19:13.973Z pw:browser [pid=113][err] [113:113:0816/191913.972365:ERROR:env.cc(255)] The platform failed to initialize.  Exiting.
playwright_python_1  | 2022-08-16T19:19:13.985Z pw:browser [pid=113] <gracefully close start>
playwright_python_1  | 2022-08-16T19:19:13.986Z pw:browser [pid=113] <kill>
playwright_python_1  | 2022-08-16T19:19:13.986Z pw:browser [pid=113] <will force kill>
playwright_python_1  | 2022-08-16T19:19:13.986Z pw:browser [pid=113] <process did exit: exitCode=1, signal=null>
playwright_python_1  | 2022-08-16T19:19:13.986Z pw:browser [pid=113] starting temporary directories cleanup
playwright_python_1  | 2022-08-16T19:19:13.992Z pw:browser [pid=113] finished temporary directories cleanup
playwright_python_1  | 2022-08-16T19:19:13.992Z pw:browser [pid=113] <gracefully close end>
playwright_python_1  | _______________ ERROR at setup of test_example_with_page_fixture _______________
playwright_python_1  | 
playwright_python_1  |     @pytest.fixture()
playwright_python_1  |     def context():
playwright_python_1  |         with sync_playwright() as playwright:
playwright_python_1  | >           playwright_browser = playwright.chromium.launch(headless=True)
playwright_python_1  | 
playwright_python_1  | test_example.py:14: 
playwright_python_1  | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/sync_api/_generated.py:11690: in launch
playwright_python_1  |     self._sync(
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_browser_type.py:93: in launch
playwright_python_1  |     Browser, from_channel(await self._channel.send("launch", params))
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_connection.py:43: in send
playwright_python_1  |     return await self._connection.wrap_api_call(
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_connection.py:387: in wrap_api_call
playwright_python_1  |     return await cb()
playwright_python_1  | _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
playwright_python_1  | 
playwright_python_1  | self = <playwright._impl._connection.Channel object at 0x7fba05edc100>
playwright_python_1  | method = 'launch', params = {'headless': True}, return_as_dict = False
playwright_python_1  | 
playwright_python_1  |     async def inner_send(
playwright_python_1  |         self, method: str, params: Optional[Dict], return_as_dict: bool
playwright_python_1  |     ) -> Any:
playwright_python_1  |         if params is None:
playwright_python_1  |             params = {}
playwright_python_1  |         callback = self._connection._send_message_to_server(self._guid, method, params)
playwright_python_1  |         if self._connection._error:
playwright_python_1  |             error = self._connection._error
playwright_python_1  |             self._connection._error = None
playwright_python_1  |             raise error
playwright_python_1  |         done, _ = await asyncio.wait(
playwright_python_1  |             {
playwright_python_1  |                 self._connection._transport.on_error_future,
playwright_python_1  |                 callback.future,
playwright_python_1  |             },
playwright_python_1  |             return_when=asyncio.FIRST_COMPLETED,
playwright_python_1  |         )
playwright_python_1  |         if not callback.future.done():
playwright_python_1  |             callback.future.cancel()
playwright_python_1  | >       result = next(iter(done)).result()
playwright_python_1  | E       playwright._impl._api_types.Error: 
playwright_python_1  | E       ╔════════════════════════════════════════════════════════════════════════════════════════════════╗
playwright_python_1  | E       ║ Looks like you launched a headed browser without having a XServer running.                     ║
playwright_python_1  | E       ║ Set either 'headless: true' or use 'xvfb-run <your-playwright-app>' before running Playwright. ║
playwright_python_1  | E       ║                                                                                                ║
playwright_python_1  | E       ║ <3 Playwright Team                                                                             ║
playwright_python_1  | E       ╚════════════════════════════════════════════════════════════════════════════════════════════════╝
playwright_python_1  | E       =========================== logs ===========================
playwright_python_1  | E       <launching> /ms-playwright/chromium-1019/chrome-linux/chrome --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-wDhIcw --remote-debugging-pipe --no-startup-window
playwright_python_1  | E       <launched> pid=236
playwright_python_1  | E       [pid=236][err] [236:236:0816/191914.513062:ERROR:ozone_platform_x11.cc(240)] Missing X server or $DISPLAY
playwright_python_1  | E       [pid=236][err] [236:236:0816/191914.513130:ERROR:env.cc(255)] The platform failed to initialize.  Exiting.
playwright_python_1  | E       ============================================================
playwright_python_1  | 
playwright_python_1  | /usr/local/lib/python3.8/dist-packages/playwright/_impl/_connection.py:78: Error
playwright_python_1  | ---------------------------- Captured stderr setup -----------------------------
playwright_python_1  | 2022-08-16T19:19:14.463Z pw:browser <launching> /ms-playwright/chromium-1019/chrome-linux/chrome --disable-field-trial-config --disable-background-networking --enable-features=NetworkService,NetworkServiceInProcess --disable-background-timer-throttling --disable-backgrounding-occluded-windows --disable-back-forward-cache --disable-breakpad --disable-client-side-phishing-detection --disable-component-extensions-with-background-pages --disable-default-apps --disable-dev-shm-usage --disable-extensions --disable-features=ImprovedCookieControls,LazyFrameLoading,GlobalMediaControls,DestroyProfileOnBrowserClose,MediaRouter,DialMediaRouteProvider,AcceptCHFrame,AutoExpandDetailsElement,CertificateTransparencyComponentUpdater,AvoidUnnecessaryBeforeUnloadCheckSync,Translate --allow-pre-commit-input --disable-hang-monitor --disable-ipc-flooding-protection --disable-popup-blocking --disable-prompt-on-repost --disable-renderer-backgrounding --disable-sync --force-color-profile=srgb --metrics-recording-only --no-first-run --enable-automation --password-store=basic --use-mock-keychain --no-service-autorun --export-tagged-pdf --no-sandbox --user-data-dir=/tmp/playwright_chromiumdev_profile-wDhIcw --remote-debugging-pipe --no-startup-window
playwright_python_1  | 2022-08-16T19:19:14.466Z pw:browser <launched> pid=236
playwright_python_1  | 2022-08-16T19:19:14.513Z pw:browser [pid=236][err] [236:236:0816/191914.513062:ERROR:ozone_platform_x11.cc(240)] Missing X server or $DISPLAY
playwright_python_1  | 2022-08-16T19:19:14.513Z pw:browser [pid=236][err] [236:236:0816/191914.513130:ERROR:env.cc(255)] The platform failed to initialize.  Exiting.
playwright_python_1  | 2022-08-16T19:19:14.522Z pw:browser [pid=236] <gracefully close start>
playwright_python_1  | 2022-08-16T19:19:14.523Z pw:browser [pid=236] <kill>
playwright_python_1  | 2022-08-16T19:19:14.523Z pw:browser [pid=236] <will force kill>
playwright_python_1  | 2022-08-16T19:19:14.524Z pw:browser [pid=236] <process did exit: exitCode=1, signal=null>
playwright_python_1  | 2022-08-16T19:19:14.524Z pw:browser [pid=236] starting temporary directories cleanup
playwright_python_1  | 2022-08-16T19:19:14.529Z pw:browser [pid=236] finished temporary directories cleanup
playwright_python_1  | 2022-08-16T19:19:14.529Z pw:browser [pid=236] <gracefully close end>
playwright_python_1  | =========================== short test summary info ============================
playwright_python_1  | ERROR test_example.py::test_example_with_context_fixture - playwright._impl._...
playwright_python_1  | ERROR test_example.py::test_example_with_page_fixture - playwright._impl._api...
playwright_python_1  | ========================= 1 passed, 2 errors in 1.55s ==========================
playwright-python-docker-example_playwright_python_1 exited with code 1
```