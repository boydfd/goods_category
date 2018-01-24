1. 处理词库，将英文都去掉

	goods_process.py: dict_preprocessor
	
2. 处理货物名，将货物名去重保存
	
	goods_cut.py: cut_goods
	
3. 将分类的百科都下载下来

	categorize.py: get_omitted_baike_links
	
4. 爬取相应的百科

	crawler.py: crawl
	
5. 解析html
