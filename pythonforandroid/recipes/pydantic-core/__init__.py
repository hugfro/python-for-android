from pythonforandroid.recipe import RustCompiledComponentsRecipe
from pythonforandroid.logger import info


class PydanticcoreRecipe(RustCompiledComponentsRecipe):
    version = "2.16.1"
    url = "https://files.pythonhosted.org/packages/d1/43/430e8a0be9dfec1ff9fb7f2289da9bd684fdb8d15796888a53b540c5e3d6/pydantic_core-2.16.3-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl"
    use_maturin = True
    hostpython_prerequisites = ["typing_extensions"]
    info("fungera tack")

    def should_build(self, arch):
        name = self.folder_name
        if self.ctx.has_package(name.replace("-", "_"), arch):
            info('Python package already exists in site-packages')
            return True
        info('{} apparently isn\'t already in site-packages'.format(name))
        return True


recipe = PydanticcoreRecipe()
