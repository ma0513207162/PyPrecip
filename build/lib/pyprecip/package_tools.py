
__all__ = ('Exporter',)


class Exporter:
    def __init__(self, globls):
        """Initialize the Exporter."""
        self.globls = globls
        self.exports = globls.setdefault('__all__', [])

    def export(self, defn):
        """声明一个导出的函数或类。"""
        self.exports.append(defn.__name__)
        return defn
                
    def __enter__(self):
        """启动一个块，跟踪在全局范围内创建的所有实例。"""
        self.start_vars = set(self.globls)          

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出实例跟踪块。"""
        self.exports.extend(set(self.globls) - self.start_vars)
        del self.start_vars


def set_module(globls):
    """
    为' ' __all__ ' '中的所有函数设置模块。
    这将设置' ' __all__ ' '列表中所有项目的' ' __module__ ' '属性
    调用模块。

    这支持我们从单个模块中提升函数，这些模块是
    考虑到实现细节，放到顶级子包的名称空间中。

    参数
    ----------
    globs: Dict[str, object]
        模块中所有全局变量的映射。这包含了所有需要的
        需要修改Python特殊("dunder")变量。
    """
    for item in globls['__all__']:
        obj = globls[item]
        if hasattr(obj, '__module__'):
            obj.__module__ = globls['__name__']
