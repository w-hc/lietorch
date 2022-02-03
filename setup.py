from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

import os.path as osp


ROOT = osp.dirname(osp.abspath(__file__))

setup(
    name='lietorch',
    version='0.2',
    description='Lie Groups for PyTorch',
    author='teedrz',
    packages=['lietorch'],
    ext_modules=[
        CppExtension(
            'lietorch_backends',
            include_dirs=[
                osp.join(ROOT, 'lietorch/include'),
                osp.join(ROOT, 'eigen')],
            sources=[
                'lietorch/src/lietorch.cpp',
                'lietorch/src/lietorch_cpu.cpp'],
            extra_compile_args={
                'cxx': ['-O2'],
            }
        ),
    ],
    cmdclass={ 'build_ext': BuildExtension }
)
