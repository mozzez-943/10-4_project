@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
    set SPHINXBUILD=sphinx-build
)

REM Set the source directory to docs/source
set SOURCEDIR=source
set BUILDDIR=_build

REM Build the documentation using Sphinx
%SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

goto end

:end
popd
