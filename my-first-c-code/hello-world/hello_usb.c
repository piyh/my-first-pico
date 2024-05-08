/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"
#include <string.h>

int sleepInterval = 1000;
int test_pin = 0;

int main()
{
  stdio_init_all();
  if (cyw43_arch_init())
  {
    printf("Wi-Fi init failed");
    return -1;
  }
  gpio_init(test_pin);
  gpio_set_dir(test_pin, GPIO_OUT);

  while (true)
  {
    // blink the onboard LED as well as GPIO pin 1
    printf("Hello, world!  Bringing pin %d up as well as the built in LED!\n", test_pin);
    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
    gpio_put(test_pin, 1);
    sleep_ms(sleepInterval);

    cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
    gpio_put(test_pin, 0);
    sleep_ms(sleepInterval);

    if (test_pin == 0){
      test_pin = 1;
    }
    else if (test_pin == 1){
      test_pin = 0;
    }
  }
}
