from scripts.shellcalls import *

install("ruby-full")
install("build-essential")
install("zlib1g-dev")
call("sudo gem install jekyll bundler")
