# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 3)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Set the input values you want to test
    dut.ui_in.value = 20
    dut.uio_in.value = 30

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 3)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    #assert dut.uo_out.value == 8
    assert concatenated_value == 8

    await ClockCycles(dut.clk, 2)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    #assert dut.uo_out.value == 8
    assert concatenated_value == 2
    

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
