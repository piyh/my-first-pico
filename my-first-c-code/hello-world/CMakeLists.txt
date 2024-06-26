cmake_minimum_required(VERSION 3.13)

# # initialize the SDK based on PICO_SDK_PATH
# # note: this must happen before project()
include(pico_sdk_import.cmake)
include_directories(${PICO_SDK_PATH}/src/rp2_common/pico_cyw43_arch/include)

project(hello_usb C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)


# initialize the Raspberry Pi Pico SDK
pico_sdk_init()


if (TARGET tinyusb_device)
    add_executable(hello_usb
            hello_usb.c
            )

    # pull in common dependencies
    target_link_libraries(hello_usb pico_stdlib
            pico_stdlib              # for core functionality
            pico_cyw43_arch_none     # we need Wifi to access the GPIO, but we don't need anything else
            )
            
    # enable usb output, disable uart output
    pico_enable_stdio_usb(hello_usb 1)
    pico_enable_stdio_uart(hello_usb 0)

    # create map/bin/hex/uf2 file etc.
    pico_add_extra_outputs(hello_usb)

elseif(PICO_ON_DEVICE)
    message(WARNING "not building hello_usb because TinyUSB submodule is not initialized in the SDK")
endif()
