
import os
import math
import random
import logging
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, Edge, RisingEdge, FallingEdge, ClockCycles
from cocotb_tools.runner import get_runner

from globefish_defaults import *

TEST_MODULE = "test_toggle"
FIRMWARE = '../firmware/test_toggle/build/firmware.hex'

first_test = True

@cocotb.parametrize(core=[1,2,4,8])
async def test_toggle(dut, core):
    """Run the simple test"""
    global first_test
    logger = logging.getLogger("test_toggle")
    logger.info("Startup sequence...")
    await start_up(dut, core, from_reset=first_test)
    first_test = False
    logger.info("Running the test...")

    toggle_count = 0
    async def mon():
        nonlocal toggle_count
        prev_val = int(dut.gpo.value[0])
        while True:
            await RisingEdge(dut.clk)
            curr_val = int(dut.gpo.value[0])
            if curr_val != prev_val:
                toggle_count += 1
            prev_val = curr_val
    
    monitor_task = cocotb.start_soon(mon())
    await ClockCycles(dut.clk, 15000//int(math.log2(1+core)))
    monitor_task.cancel()

    logger.info("[RESULT] GPO[0] toggled {} times.".format(toggle_count))
    assert toggle_count > 10
    
if __name__ == "__main__":
    sim_setup(TEST_MODULE, FIRMWARE)