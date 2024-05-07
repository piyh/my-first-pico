# Install Prereqs

`brew install cmake minicom`

Make sure the normal ARM toolchain is not present on M series macs.
`brew uninstall arm-none-eabi-gcc && brew autoremove`

Toolchain install 
`brew tap ArmMbed/homebrew-formulae`

`brew install gcc-arm-embedded`


# Clone Repos 

`git clone https://github.com/raspberrypi/pico-sdk.git`

`git clone https://github.com/raspberrypi/pico-examples`

`git clone https://github.com/raspberrypi/pico-extras.git`

In your `pico-sdk` , run `git submodule update --init`

add this to your `.bashrc` or `.zshrc` file: `PICO_SDK_PATH=/Users/ryan/Desktop/Files/repos/pico-sdk`

# Build

Navigate to `./my-first-c-code/blink`, run 

`cmake .. -DPICO_BOARD=pico_w && make`

# Run Blink

Restart the Pico W while holding BOOTSEL button.

Copy built `.uf2` file to pico.  Pico will restart and code will run

`cp picow_blink.uf2 /Volumes/RPI-RP2/.`


# Hello World - TTY debugging

`cd my-first-c-code/hello-world/build`

`cmake .. -DPICO_BOARD=pico_w && make`

`cp hello_usb.uf2 /Volumes/RPI-RP2/.`

`TERM=xterm screen /dev/tty.usbmodem101 115200`

Control + A, then Control + \ to quit screen.


# When things go wrong!

If you don't run your code in an infinite loop, you may find the pi hard to interact with via Thonny or your normal copy a .`uf2` file to the drive.  If that's the case, copy the `flash_nuke.uf2` to the pico and it'll be reset to it's factory state.