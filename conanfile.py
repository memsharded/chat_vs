from conans import ConanFile, MSBuild


class ChatConan(ConanFile):
    name = "Chat"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/memsharded/chat_vs"
    requires = "Hello/0.1@memsharded/testing"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "src/*", "build/*"
    generators = "visual_studio"

    def build(self):
        msbuild = MSBuild(self)
        msbuild.build("build/ChatLib/ChatLib.sln")

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ChatLib"]
