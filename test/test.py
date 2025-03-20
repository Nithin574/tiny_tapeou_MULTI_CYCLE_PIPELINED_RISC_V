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

   
    await ClockCycles(dut.clk, 3)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    #dut._log.info(f"Test Case 1: Expected 8, Got {int(dut.out)}")    
    assert dut.out == 8#, f"Test Case 1 Failed: Expected 8, Got {int(dut.out)}"

    await ClockCycles(dut.clk, 2)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 2: Expected 2, Got {int(concatenated_value)}")    
    assert concatenated_value == 2, f"Test Case 2 Failed: Expected 2, Got {int(concatenated_value)}"

    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 3: Expected 10, Got {int(concatenated_value)}")    
    assert concatenated_value == 10, f"Test Case 3 Failed: Expected 10, Got {int(concatenated_value)}"

    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 4: Expected 6, Got {int(concatenated_value)}")    
    assert concatenated_value == 6, f"Test Case 4 Failed: Expected 6, Got {int(concatenated_value)}"
   
    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 5: Expected 0, Got {int(concatenated_value)}")    
    assert concatenated_value == 0, f"Test Case 5 Failed: Expected 0, Got {int(concatenated_value)}"
  
    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 6: Expected 10, Got {int(concatenated_value)}")    
    assert concatenated_value == 10, f"Test Case 6 Failed: Expected 10, Got {int(concatenated_value)}"
   
    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 7: Expected 10, Got {int(concatenated_value)}")    
    assert concatenated_value == 10, f"Test Case 7 Failed: Expected 10, Got {int(concatenated_value)}"
 
    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 8: Expected 12, Got {int(concatenated_value)}")    
    assert concatenated_value == 12, f"Test Case 8 Failed: Expected 12, Got {int(concatenated_value)}"

    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 9: Expected 20, Got {int(concatenated_value)}")    
    assert concatenated_value == 20, f"Test Case 9 Failed: Expected 20, Got {int(concatenated_value)}"

    await ClockCycles(dut.clk, 1)
    concatenated_value = (dut.uio_out.value.integer << 8) | dut.uo_out.value.integer
    dut._log.info(f"Test Case 10: Expected 0, Got {int(concatenated_value)}")    
    assert concatenated_value == 0, f"Test Case 10 Failed: Expected 0, Got {int(concatenated_value)}"

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
