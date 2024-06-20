### 更新文档，包括故障排除步骤

### 概览

该 Python 脚本用于自动化从 Bing 搜索引擎根据用户定义的搜索关键字抓取和下载图片。它使用了如 Selenium 用于网页导航、PIL 用于图片处理和 pandas 用于数据管理等库。通过 argparse 支持命令行参数，为不同的搜索查询提供灵活性。

### 系统要求

- Python 3.x
- Selenium
- pandas
- Pillow (PIL Fork)
- tqdm
- urllib

确保你已经安装了 Chrome WebDriver，并且正确设置在系统的 PATH 中。

### 安装

1. 安装必要的 Python 包：
   ```bash
   pip install selenium pandas Pillow tqdm urllib3
   ```

2. 下载并安装 Chrome WebDriver。确保它与你系统中安装的 Chrome 版本相匹配。你可以从 [Chrome WebDriver](https://sites.google.com/chromium.org/driver/home) 下载它。

### 运行脚本

在命令行中执行脚本，添加搜索关键字作为参数：
```bash
python image_crawler.py "Birds"
```
将 `"Birds"` 替换为你选择的搜索关键词。

### 脚本工作流程

![WindowsTerminalDemo](WindowsTerminalDemo.gif)

1. **初始化**：解析命令行参数以获取搜索关键词，并设置存储图片和链接的目录。
2. **Selenium WebDriver 设置**：初始化 Chrome WebDriver 以与 Bing 的图片搜索交互。
3. **搜索和导航**：导航至 Bing 图片，输入搜索词，并调整 URL 以筛选特定的图片特征。
4. **滚动和交互**：模拟页面滚动并点击“查看更多”按钮以加载更多图片。
5. **图片爬取和下载**：
   - 从图片缩略图中提取 URL。
   - 将图片下载到指定目录。
6. **链接存储**：将收集到的图片 URL 保存在一个单独的目录中的 CSV 文件里。
7. **清理**：在关闭浏览器之前包含了显著的延迟，用于演示目的。

### 故障排除

#### 常见问题

如果你遇到以下错误：

```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 111
```

这表明 ChromeDriver 与你安装的 Chrome 版本之间存在版本不匹配。

#### 解决方案

1. 通过导航至你的 Chrome 浏览器的 `chrome://settings/help` 来确定你的 Chrome 版本。
2. 访问以下链接，找到并下载与你的 Chrome 版本相对应的 ChromeDriver：
   - [ChromeDriver - WebDriver for Chrome](https://sites.google.com/chromium.org/driver/home)
   - [ChromeDriver - Downloads](https://sites.google.com/chromium.org/driver/downloads)
如果你使用的是 Chrome 版本 115 或更新，请查阅 Chrome for Testing 可用性仪表板。
   - [ChromeDriver - Downloads 115 or newer](https://googlechromelabs.github.io/chrome-for-testing/)
该页面为特定 ChromeDriver 版本的下载提供了便捷的 JSON 端点。
3. 用下载的版本替换项目文件夹中现有的 `chromedriver.exe`。

### 注意事项

- **错误处理**：包含了基本的错误处理，但你可能需要针对特定用例增强机制。
- **执行时间**：集成了 `time.sleep` 延迟，以模仿人类的交互速度；根据你的需求调整这些延迟。
- **存储要求**：确保有足够的存储空间用于下载的图片，并适当管理目录以适应多次搜索会话。

