# geoJson-cn

python爬虫获取中国-省-市-区县的geoJSON格式地图数据

爬取日期： 2021-02-05

对应文件夹解释:
- 全国地图-包含子区域: data/country_full
- 全国地图-外轮廓: data/country
- 全国各省地图-包含子区域：data/province_full
- 全国各省地图-外轮廓：data/province
- 全国各市地图-包含子区域：data/city_full
- 全国各市地图-外轮廓：data/city
- 全国各区县地图-外轮廓：data/county
- 全国省市区县所对应行政区划代码以及中心点的坐标：location.json (方便用于echarts上显示某个点的位置)可直接用于echarts地图的显示
  

数据来源： http://datav.aliyun.com/tools/atlas/