# pyprecip 相关记录

pyprecip 是一个用于处理气候数据的 Python 库。它提供了一系列功能，可以帮助您轻松地读取、处理、分析和可视化气候数据。

设计模式： 单例模式   开发模式：敏捷开发模式

受众群体：任何想要编写python脚本来进行气候数据处理的人

相关项目： [MetPy、pygrib、iris、geopandas、cdsapi]([Your list / IndependentDevelopment (github.com)](https://github.com/stars/ma0513207162/lists/independentdevelopment))

# 需求整理

## 一、基本功能的实现 

### 1、数据读取

- 支持读取各种格式的气候数据文件，例如：NetCDF、GRIB、HDF、HDF5、CSV、Excel
- 支持从气象数据 API 中读取数据，例如：NOAA API、NCEI API、Copernicus API
- 支持多种数据来源,如地面站点观测、卫星遥感、模型输出等
- 输入指定的行政区划代码、时间、获取实时的气候数据，支持转换不同的样式在终端显示输出 

### 2、数据预处理与变换

- 数据进行清洗和预处理，例如缺失值处理、异常值处理（检测和过滤）
- 数据转换：单位与数据格式转换（json数据的转换）、时间处理(如转换时区、重采样等)
- 数据进行统计分析，例如：计算基本统计量、绘制统计图 ：直方图、散点图、箱型图、
- 数据进行时空分析，例如：空间插值、时间序列分析
- 常用气候指标计算,如平均值、中位数、标准差、极值等

### 3、数据可视化

- 使用地图进行可视化，支持使用绘制等值线图、矢量图、散点图进行可视化
- 使用图表进行可视化，例如绘制折线图、柱状图、饼状图
- 生成动画，例如制作时间序列动画、空间演变动画

### 4、气候数据的导出和存储

- 将数据导出到各种格式的文件，例如 NetCDF、CSV、Excel 等。
- 编写自定义函数，以满足特定需求。

### 5、降水量（precipitation）的相关实现

- 读取更多格式的降水数据文件，例如 GPCP、CMORPH 等。
- 更多降水数据的统计分析方法，例如计算降水量集中度、分析降水事件、评估降水预报的准确性

- 使用更多地图类型进行可视化，例如等值线图、分级图、3D 地图
- 将降水数据与其他气象数据进行融合，例如分析降水与温度的关系、分析降水与风的关系

## 二、 官网开发

### 基本的功能实现

- html 使用文档的撰写
- 数据可视化的演示 
- .........


