

template = """
define_pdn_grid \\
    -macro \\
    -instances {} \\
    -name {} \\
    -starts_with POWER \\
    -halo "$::env(PDN_HORIZONTAL_HALO) $::env(PDN_VERTICAL_HALO)"

add_pdn_connect \\
    -grid {} \\
    -layers "$::env(PDN_VERTICAL_LAYER) $::env(PDN_HORIZONTAL_LAYER)"

add_pdn_connect \\
    -grid {} \\
    -layers "$::env(PDN_VERTICAL_LAYER) Metal3"

add_pdn_stripe -grid {} -layer Metal4 -width 2.36 -offset 1.18 -spacing 0.28 -pitch 426.86 -starts_with GROUND -number_of_straps 2

"""

sram_macros = ["i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[0].i_ram512x32.gen_ram8[0].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[0].i_ram512x32.gen_ram8[1].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[0].i_ram512x32.gen_ram8[2].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[0].i_ram512x32.gen_ram8[3].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[1].i_ram512x32.gen_ram8[0].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[1].i_ram512x32.gen_ram8[1].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[1].i_ram512x32.gen_ram8[2].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[1].i_ram512x32.gen_ram8[3].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[2].i_ram512x32.gen_ram8[0].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[2].i_ram512x32.gen_ram8[1].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[2].i_ram512x32.gen_ram8[2].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[2].i_ram512x32.gen_ram8[3].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[3].i_ram512x32.gen_ram8[0].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[3].i_ram512x32.gen_ram8[1].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[3].i_ram512x32.gen_ram8[2].u_ram.sram_0",
                "i_chip_core.i_globefish_soc.i_wb_ram.gen_ram_bank[3].i_ram512x32.gen_ram8[3].u_ram.sram_0"]


for i, sram in enumerate(sram_macros):
    name = "sram_macro_{}_{}".format(i//4, i%4)
    print(template.format(sram, name, name, name, name))