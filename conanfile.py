from conans import ConanFile, tools


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
        cmd = tools.msvc_build_command(self.settings, "build/ChatLib/ChatLib.sln")
        self.run(cmd)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ChatLib"]
