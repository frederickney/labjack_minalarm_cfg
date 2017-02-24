__author__ = 'Frederick NEY'
from labjack import ljm
import LabjackT7Lib as Kernel

"""
/**********************************************************************************************************************/
/****************************************************USEFUL VARIABLES**************************************************/
/**********************************************************************************************************************/
"""

DAC_ADDRS = [
    Kernel.T7_DAC0, Kernel.T7_DAC1
]

RES_LIST = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
]

SETTLING_LIST = [
    10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000
]

RES_ADDR = [
    Kernel.T7_AIN0_RESOLUTION_INDEX, Kernel.T7_AIN1_RESOLUTION_INDEX, Kernel.T7_AIN2_RESOLUTION_INDEX,
    Kernel.T7_AIN3_RESOLUTION_INDEX, Kernel.T7_AIN4_RESOLUTION_INDEX, Kernel.T7_AIN5_RESOLUTION_INDEX,
    Kernel.T7_AIN6_RESOLUTION_INDEX, Kernel.T7_AIN7_RESOLUTION_INDEX, Kernel.T7_AIN8_RESOLUTION_INDEX,
    Kernel.T7_AIN9_RESOLUTION_INDEX, Kernel.T7_AIN10_RESOLUTION_INDEX, Kernel.T7_AIN11_RESOLUTION_INDEX,
    Kernel.T7_AIN12_RESOLUTION_INDEX, Kernel.T7_AIN13_RESOLUTION_INDEX, Kernel.T7_AIN14_RESOLUTION_INDEX,
    Kernel.T7_AIN15_RESOLUTION_INDEX, Kernel.T7_AIN16_RESOLUTION_INDEX, Kernel.T7_AIN17_RESOLUTION_INDEX,
    Kernel.T7_AIN18_RESOLUTION_INDEX, Kernel.T7_AIN19_RESOLUTION_INDEX, Kernel.T7_AIN20_RESOLUTION_INDEX,
    Kernel.T7_AIN21_RESOLUTION_INDEX, Kernel.T7_AIN22_RESOLUTION_INDEX, Kernel.T7_AIN23_RESOLUTION_INDEX,
    Kernel.T7_AIN24_RESOLUTION_INDEX, Kernel.T7_AIN25_RESOLUTION_INDEX, Kernel.T7_AIN26_RESOLUTION_INDEX,
    Kernel.T7_AIN27_RESOLUTION_INDEX, Kernel.T7_AIN28_RESOLUTION_INDEX, Kernel.T7_AIN29_RESOLUTION_INDEX,
    Kernel.T7_AIN30_RESOLUTION_INDEX, Kernel.T7_AIN31_RESOLUTION_INDEX, Kernel.T7_AIN32_RESOLUTION_INDEX,
    Kernel.T7_AIN33_RESOLUTION_INDEX, Kernel.T7_AIN34_RESOLUTION_INDEX, Kernel.T7_AIN35_RESOLUTION_INDEX,
    Kernel.T7_AIN36_RESOLUTION_INDEX, Kernel.T7_AIN37_RESOLUTION_INDEX, Kernel.T7_AIN38_RESOLUTION_INDEX,
    Kernel.T7_AIN39_RESOLUTION_INDEX, Kernel.T7_AIN40_RESOLUTION_INDEX, Kernel.T7_AIN41_RESOLUTION_INDEX,
    Kernel.T7_AIN42_RESOLUTION_INDEX, Kernel.T7_AIN43_RESOLUTION_INDEX, Kernel.T7_AIN44_RESOLUTION_INDEX,
    Kernel.T7_AIN45_RESOLUTION_INDEX, Kernel.T7_AIN46_RESOLUTION_INDEX, Kernel.T7_AIN47_RESOLUTION_INDEX,
    Kernel.T7_AIN48_RESOLUTION_INDEX, Kernel.T7_AIN49_RESOLUTION_INDEX, Kernel.T7_AIN50_RESOLUTION_INDEX,
    Kernel.T7_AIN51_RESOLUTION_INDEX, Kernel.T7_AIN52_RESOLUTION_INDEX, Kernel.T7_AIN53_RESOLUTION_INDEX,
    Kernel.T7_AIN54_RESOLUTION_INDEX, Kernel.T7_AIN55_RESOLUTION_INDEX, Kernel.T7_AIN56_RESOLUTION_INDEX,
    Kernel.T7_AIN57_RESOLUTION_INDEX, Kernel.T7_AIN58_RESOLUTION_INDEX, Kernel.T7_AIN59_RESOLUTION_INDEX,
    Kernel.T7_AIN60_RESOLUTION_INDEX, Kernel.T7_AIN61_RESOLUTION_INDEX, Kernel.T7_AIN62_RESOLUTION_INDEX,
    Kernel.T7_AIN63_RESOLUTION_INDEX, Kernel.T7_AIN64_RESOLUTION_INDEX, Kernel.T7_AIN65_RESOLUTION_INDEX,
    Kernel.T7_AIN66_RESOLUTION_INDEX, Kernel.T7_AIN67_RESOLUTION_INDEX, Kernel.T7_AIN68_RESOLUTION_INDEX,
    Kernel.T7_AIN69_RESOLUTION_INDEX, Kernel.T7_AIN70_RESOLUTION_INDEX, Kernel.T7_AIN71_RESOLUTION_INDEX,
    Kernel.T7_AIN72_RESOLUTION_INDEX, Kernel.T7_AIN73_RESOLUTION_INDEX, Kernel.T7_AIN74_RESOLUTION_INDEX,
    Kernel.T7_AIN75_RESOLUTION_INDEX, Kernel.T7_AIN76_RESOLUTION_INDEX, Kernel.T7_AIN77_RESOLUTION_INDEX,
    Kernel.T7_AIN78_RESOLUTION_INDEX, Kernel.T7_AIN79_RESOLUTION_INDEX, Kernel.T7_AIN80_RESOLUTION_INDEX,
    Kernel.T7_AIN81_RESOLUTION_INDEX, Kernel.T7_AIN82_RESOLUTION_INDEX, Kernel.T7_AIN83_RESOLUTION_INDEX,
    Kernel.T7_AIN84_RESOLUTION_INDEX, Kernel.T7_AIN85_RESOLUTION_INDEX, Kernel.T7_AIN86_RESOLUTION_INDEX,
    Kernel.T7_AIN87_RESOLUTION_INDEX, Kernel.T7_AIN88_RESOLUTION_INDEX, Kernel.T7_AIN89_RESOLUTION_INDEX,
    Kernel.T7_AIN90_RESOLUTION_INDEX, Kernel.T7_AIN91_RESOLUTION_INDEX, Kernel.T7_AIN92_RESOLUTION_INDEX,
    Kernel.T7_AIN93_RESOLUTION_INDEX, Kernel.T7_AIN94_RESOLUTION_INDEX, Kernel.T7_AIN95_RESOLUTION_INDEX,
    Kernel.T7_AIN96_RESOLUTION_INDEX, Kernel.T7_AIN97_RESOLUTION_INDEX, Kernel.T7_AIN98_RESOLUTION_INDEX,
    Kernel.T7_AIN99_RESOLUTION_INDEX, Kernel.T7_AIN100_RESOLUTION_INDEX, Kernel.T7_AIN101_RESOLUTION_INDEX,
    Kernel.T7_AIN102_RESOLUTION_INDEX, Kernel.T7_AIN103_RESOLUTION_INDEX, Kernel.T7_AIN104_RESOLUTION_INDEX,
    Kernel.T7_AIN105_RESOLUTION_INDEX, Kernel.T7_AIN106_RESOLUTION_INDEX, Kernel.T7_AIN107_RESOLUTION_INDEX,
    Kernel.T7_AIN108_RESOLUTION_INDEX, Kernel.T7_AIN109_RESOLUTION_INDEX, Kernel.T7_AIN110_RESOLUTION_INDEX,
    Kernel.T7_AIN111_RESOLUTION_INDEX, Kernel.T7_AIN112_RESOLUTION_INDEX, Kernel.T7_AIN113_RESOLUTION_INDEX,
    Kernel.T7_AIN114_RESOLUTION_INDEX, Kernel.T7_AIN115_RESOLUTION_INDEX, Kernel.T7_AIN116_RESOLUTION_INDEX,
    Kernel.T7_AIN117_RESOLUTION_INDEX, Kernel.T7_AIN118_RESOLUTION_INDEX, Kernel.T7_AIN119_RESOLUTION_INDEX,
    Kernel.T7_AIN120_RESOLUTION_INDEX, Kernel.T7_AIN121_RESOLUTION_INDEX, Kernel.T7_AIN122_RESOLUTION_INDEX,
    Kernel.T7_AIN123_RESOLUTION_INDEX, Kernel.T7_AIN124_RESOLUTION_INDEX, Kernel.T7_AIN125_RESOLUTION_INDEX,
    Kernel.T7_AIN126_RESOLUTION_INDEX, Kernel.T7_AIN127_RESOLUTION_INDEX, Kernel.T7_AIN128_RESOLUTION_INDEX,
    Kernel.T7_AIN129_RESOLUTION_INDEX, Kernel.T7_AIN130_RESOLUTION_INDEX, Kernel.T7_AIN131_RESOLUTION_INDEX,
    Kernel.T7_AIN132_RESOLUTION_INDEX, Kernel.T7_AIN133_RESOLUTION_INDEX, Kernel.T7_AIN134_RESOLUTION_INDEX,
    Kernel.T7_AIN135_RESOLUTION_INDEX, Kernel.T7_AIN136_RESOLUTION_INDEX, Kernel.T7_AIN137_RESOLUTION_INDEX,
    Kernel.T7_AIN138_RESOLUTION_INDEX, Kernel.T7_AIN139_RESOLUTION_INDEX, Kernel.T7_AIN140_RESOLUTION_INDEX,
    Kernel.T7_AIN141_RESOLUTION_INDEX, Kernel.T7_AIN142_RESOLUTION_INDEX, Kernel.T7_AIN143_RESOLUTION_INDEX,
    Kernel.T7_AIN144_RESOLUTION_INDEX, Kernel.T7_AIN145_RESOLUTION_INDEX, Kernel.T7_AIN146_RESOLUTION_INDEX,
    Kernel.T7_AIN147_RESOLUTION_INDEX, Kernel.T7_AIN148_RESOLUTION_INDEX, Kernel.T7_AIN149_RESOLUTION_INDEX,
    Kernel.T7_AIN150_RESOLUTION_INDEX, Kernel.T7_AIN151_RESOLUTION_INDEX, Kernel.T7_AIN152_RESOLUTION_INDEX,
    Kernel.T7_AIN153_RESOLUTION_INDEX, Kernel.T7_AIN154_RESOLUTION_INDEX, Kernel.T7_AIN155_RESOLUTION_INDEX,
    Kernel.T7_AIN156_RESOLUTION_INDEX, Kernel.T7_AIN157_RESOLUTION_INDEX, Kernel.T7_AIN158_RESOLUTION_INDEX,
    Kernel.T7_AIN159_RESOLUTION_INDEX, Kernel.T7_AIN160_RESOLUTION_INDEX, Kernel.T7_AIN161_RESOLUTION_INDEX,
    Kernel.T7_AIN162_RESOLUTION_INDEX, Kernel.T7_AIN163_RESOLUTION_INDEX, Kernel.T7_AIN164_RESOLUTION_INDEX,
    Kernel.T7_AIN165_RESOLUTION_INDEX, Kernel.T7_AIN166_RESOLUTION_INDEX, Kernel.T7_AIN167_RESOLUTION_INDEX,
    Kernel.T7_AIN168_RESOLUTION_INDEX, Kernel.T7_AIN169_RESOLUTION_INDEX, Kernel.T7_AIN170_RESOLUTION_INDEX,
    Kernel.T7_AIN171_RESOLUTION_INDEX, Kernel.T7_AIN172_RESOLUTION_INDEX, Kernel.T7_AIN173_RESOLUTION_INDEX,
    Kernel.T7_AIN174_RESOLUTION_INDEX, Kernel.T7_AIN175_RESOLUTION_INDEX, Kernel.T7_AIN176_RESOLUTION_INDEX,
    Kernel.T7_AIN177_RESOLUTION_INDEX, Kernel.T7_AIN178_RESOLUTION_INDEX, Kernel.T7_AIN179_RESOLUTION_INDEX,
    Kernel.T7_AIN180_RESOLUTION_INDEX, Kernel.T7_AIN181_RESOLUTION_INDEX, Kernel.T7_AIN182_RESOLUTION_INDEX,
    Kernel.T7_AIN183_RESOLUTION_INDEX, Kernel.T7_AIN184_RESOLUTION_INDEX, Kernel.T7_AIN185_RESOLUTION_INDEX,
    Kernel.T7_AIN186_RESOLUTION_INDEX, Kernel.T7_AIN187_RESOLUTION_INDEX, Kernel.T7_AIN188_RESOLUTION_INDEX,
    Kernel.T7_AIN189_RESOLUTION_INDEX, Kernel.T7_AIN190_RESOLUTION_INDEX, Kernel.T7_AIN191_RESOLUTION_INDEX,
    Kernel.T7_AIN192_RESOLUTION_INDEX, Kernel.T7_AIN193_RESOLUTION_INDEX, Kernel.T7_AIN194_RESOLUTION_INDEX,
    Kernel.T7_AIN195_RESOLUTION_INDEX, Kernel.T7_AIN196_RESOLUTION_INDEX, Kernel.T7_AIN197_RESOLUTION_INDEX,
    Kernel.T7_AIN198_RESOLUTION_INDEX, Kernel.T7_AIN199_RESOLUTION_INDEX, Kernel.T7_AIN200_RESOLUTION_INDEX,
    Kernel.T7_AIN201_RESOLUTION_INDEX, Kernel.T7_AIN202_RESOLUTION_INDEX, Kernel.T7_AIN203_RESOLUTION_INDEX,
    Kernel.T7_AIN204_RESOLUTION_INDEX, Kernel.T7_AIN205_RESOLUTION_INDEX, Kernel.T7_AIN206_RESOLUTION_INDEX,
    Kernel.T7_AIN207_RESOLUTION_INDEX, Kernel.T7_AIN208_RESOLUTION_INDEX, Kernel.T7_AIN209_RESOLUTION_INDEX,
    Kernel.T7_AIN210_RESOLUTION_INDEX, Kernel.T7_AIN211_RESOLUTION_INDEX, Kernel.T7_AIN212_RESOLUTION_INDEX,
    Kernel.T7_AIN213_RESOLUTION_INDEX, Kernel.T7_AIN214_RESOLUTION_INDEX, Kernel.T7_AIN215_RESOLUTION_INDEX,
    Kernel.T7_AIN216_RESOLUTION_INDEX, Kernel.T7_AIN217_RESOLUTION_INDEX, Kernel.T7_AIN218_RESOLUTION_INDEX,
    Kernel.T7_AIN219_RESOLUTION_INDEX, Kernel.T7_AIN220_RESOLUTION_INDEX, Kernel.T7_AIN221_RESOLUTION_INDEX,
    Kernel.T7_AIN222_RESOLUTION_INDEX, Kernel.T7_AIN223_RESOLUTION_INDEX, Kernel.T7_AIN224_RESOLUTION_INDEX,
    Kernel.T7_AIN225_RESOLUTION_INDEX, Kernel.T7_AIN226_RESOLUTION_INDEX, Kernel.T7_AIN227_RESOLUTION_INDEX,
    Kernel.T7_AIN228_RESOLUTION_INDEX, Kernel.T7_AIN229_RESOLUTION_INDEX, Kernel.T7_AIN230_RESOLUTION_INDEX,
    Kernel.T7_AIN231_RESOLUTION_INDEX, Kernel.T7_AIN232_RESOLUTION_INDEX, Kernel.T7_AIN233_RESOLUTION_INDEX,
    Kernel.T7_AIN234_RESOLUTION_INDEX, Kernel.T7_AIN235_RESOLUTION_INDEX, Kernel.T7_AIN236_RESOLUTION_INDEX,
    Kernel.T7_AIN237_RESOLUTION_INDEX, Kernel.T7_AIN238_RESOLUTION_INDEX, Kernel.T7_AIN239_RESOLUTION_INDEX,
    Kernel.T7_AIN240_RESOLUTION_INDEX, Kernel.T7_AIN241_RESOLUTION_INDEX, Kernel.T7_AIN242_RESOLUTION_INDEX,
    Kernel.T7_AIN243_RESOLUTION_INDEX, Kernel.T7_AIN244_RESOLUTION_INDEX, Kernel.T7_AIN245_RESOLUTION_INDEX,
    Kernel.T7_AIN246_RESOLUTION_INDEX, Kernel.T7_AIN247_RESOLUTION_INDEX, Kernel.T7_AIN248_RESOLUTION_INDEX,
    Kernel.T7_AIN249_RESOLUTION_INDEX, Kernel.T7_AIN250_RESOLUTION_INDEX, Kernel.T7_AIN251_RESOLUTION_INDEX,
    Kernel.T7_AIN252_RESOLUTION_INDEX, Kernel.T7_AIN253_RESOLUTION_INDEX, Kernel.T7_AIN254_RESOLUTION_INDEX,
    Kernel.T7_AIN_ALL_RESOLUTION_INDEX
]


SETTLING_ADDR = [
    Kernel.T7_AIN0_SETTLING_US, Kernel.T7_AIN1_SETTLING_US, Kernel.T7_AIN2_SETTLING_US,
    Kernel.T7_AIN3_SETTLING_US, Kernel.T7_AIN4_SETTLING_US, Kernel.T7_AIN5_SETTLING_US,
    Kernel.T7_AIN6_SETTLING_US, Kernel.T7_AIN7_SETTLING_US, Kernel.T7_AIN8_SETTLING_US,
    Kernel.T7_AIN9_SETTLING_US, Kernel.T7_AIN10_SETTLING_US, Kernel.T7_AIN11_SETTLING_US,
    Kernel.T7_AIN12_SETTLING_US, Kernel.T7_AIN13_SETTLING_US, Kernel.T7_AIN14_SETTLING_US,
    Kernel.T7_AIN15_SETTLING_US, Kernel.T7_AIN16_SETTLING_US, Kernel.T7_AIN17_SETTLING_US,
    Kernel.T7_AIN18_SETTLING_US, Kernel.T7_AIN19_SETTLING_US, Kernel.T7_AIN20_SETTLING_US,
    Kernel.T7_AIN21_SETTLING_US, Kernel.T7_AIN22_SETTLING_US, Kernel.T7_AIN23_SETTLING_US,
    Kernel.T7_AIN24_SETTLING_US, Kernel.T7_AIN25_SETTLING_US, Kernel.T7_AIN26_SETTLING_US,
    Kernel.T7_AIN27_SETTLING_US, Kernel.T7_AIN28_SETTLING_US, Kernel.T7_AIN29_SETTLING_US,
    Kernel.T7_AIN30_SETTLING_US, Kernel.T7_AIN31_SETTLING_US, Kernel.T7_AIN32_SETTLING_US,
    Kernel.T7_AIN33_SETTLING_US, Kernel.T7_AIN34_SETTLING_US, Kernel.T7_AIN35_SETTLING_US,
    Kernel.T7_AIN36_SETTLING_US, Kernel.T7_AIN37_SETTLING_US, Kernel.T7_AIN38_SETTLING_US,
    Kernel.T7_AIN39_SETTLING_US, Kernel.T7_AIN40_SETTLING_US, Kernel.T7_AIN41_SETTLING_US,
    Kernel.T7_AIN42_SETTLING_US, Kernel.T7_AIN43_SETTLING_US, Kernel.T7_AIN44_SETTLING_US,
    Kernel.T7_AIN45_SETTLING_US, Kernel.T7_AIN46_SETTLING_US, Kernel.T7_AIN47_SETTLING_US,
    Kernel.T7_AIN48_SETTLING_US, Kernel.T7_AIN49_SETTLING_US, Kernel.T7_AIN50_SETTLING_US,
    Kernel.T7_AIN51_SETTLING_US, Kernel.T7_AIN52_SETTLING_US, Kernel.T7_AIN53_SETTLING_US,
    Kernel.T7_AIN54_SETTLING_US, Kernel.T7_AIN55_SETTLING_US, Kernel.T7_AIN56_SETTLING_US,
    Kernel.T7_AIN57_SETTLING_US, Kernel.T7_AIN58_SETTLING_US, Kernel.T7_AIN59_SETTLING_US,
    Kernel.T7_AIN60_SETTLING_US, Kernel.T7_AIN61_SETTLING_US, Kernel.T7_AIN62_SETTLING_US,
    Kernel.T7_AIN63_SETTLING_US, Kernel.T7_AIN64_SETTLING_US, Kernel.T7_AIN65_SETTLING_US,
    Kernel.T7_AIN66_SETTLING_US, Kernel.T7_AIN67_SETTLING_US, Kernel.T7_AIN68_SETTLING_US,
    Kernel.T7_AIN69_SETTLING_US, Kernel.T7_AIN70_SETTLING_US, Kernel.T7_AIN71_SETTLING_US,
    Kernel.T7_AIN72_SETTLING_US, Kernel.T7_AIN73_SETTLING_US, Kernel.T7_AIN74_SETTLING_US,
    Kernel.T7_AIN75_SETTLING_US, Kernel.T7_AIN76_SETTLING_US, Kernel.T7_AIN77_SETTLING_US,
    Kernel.T7_AIN78_SETTLING_US, Kernel.T7_AIN79_SETTLING_US, Kernel.T7_AIN80_SETTLING_US,
    Kernel.T7_AIN81_SETTLING_US, Kernel.T7_AIN82_SETTLING_US, Kernel.T7_AIN83_SETTLING_US,
    Kernel.T7_AIN84_SETTLING_US, Kernel.T7_AIN85_SETTLING_US, Kernel.T7_AIN86_SETTLING_US,
    Kernel.T7_AIN87_SETTLING_US, Kernel.T7_AIN88_SETTLING_US, Kernel.T7_AIN89_SETTLING_US,
    Kernel.T7_AIN90_SETTLING_US, Kernel.T7_AIN91_SETTLING_US, Kernel.T7_AIN92_SETTLING_US,
    Kernel.T7_AIN93_SETTLING_US, Kernel.T7_AIN94_SETTLING_US, Kernel.T7_AIN95_SETTLING_US,
    Kernel.T7_AIN96_SETTLING_US, Kernel.T7_AIN97_SETTLING_US, Kernel.T7_AIN98_SETTLING_US,
    Kernel.T7_AIN99_SETTLING_US, Kernel.T7_AIN100_SETTLING_US, Kernel.T7_AIN101_SETTLING_US,
    Kernel.T7_AIN102_SETTLING_US, Kernel.T7_AIN103_SETTLING_US, Kernel.T7_AIN104_SETTLING_US,
    Kernel.T7_AIN105_SETTLING_US, Kernel.T7_AIN106_SETTLING_US, Kernel.T7_AIN107_SETTLING_US,
    Kernel.T7_AIN108_SETTLING_US, Kernel.T7_AIN109_SETTLING_US, Kernel.T7_AIN110_SETTLING_US,
    Kernel.T7_AIN111_SETTLING_US, Kernel.T7_AIN112_SETTLING_US, Kernel.T7_AIN113_SETTLING_US,
    Kernel.T7_AIN114_SETTLING_US, Kernel.T7_AIN115_SETTLING_US, Kernel.T7_AIN116_SETTLING_US,
    Kernel.T7_AIN117_SETTLING_US, Kernel.T7_AIN118_SETTLING_US, Kernel.T7_AIN119_SETTLING_US,
    Kernel.T7_AIN120_SETTLING_US, Kernel.T7_AIN121_SETTLING_US, Kernel.T7_AIN122_SETTLING_US,
    Kernel.T7_AIN123_SETTLING_US, Kernel.T7_AIN124_SETTLING_US, Kernel.T7_AIN125_SETTLING_US,
    Kernel.T7_AIN126_SETTLING_US, Kernel.T7_AIN127_SETTLING_US, Kernel.T7_AIN128_SETTLING_US,
    Kernel.T7_AIN129_SETTLING_US, Kernel.T7_AIN130_SETTLING_US, Kernel.T7_AIN131_SETTLING_US,
    Kernel.T7_AIN132_SETTLING_US, Kernel.T7_AIN133_SETTLING_US, Kernel.T7_AIN134_SETTLING_US,
    Kernel.T7_AIN135_SETTLING_US, Kernel.T7_AIN136_SETTLING_US, Kernel.T7_AIN137_SETTLING_US,
    Kernel.T7_AIN138_SETTLING_US, Kernel.T7_AIN139_SETTLING_US, Kernel.T7_AIN140_SETTLING_US,
    Kernel.T7_AIN141_SETTLING_US, Kernel.T7_AIN142_SETTLING_US, Kernel.T7_AIN143_SETTLING_US,
    Kernel.T7_AIN144_SETTLING_US, Kernel.T7_AIN145_SETTLING_US, Kernel.T7_AIN146_SETTLING_US,
    Kernel.T7_AIN147_SETTLING_US, Kernel.T7_AIN148_SETTLING_US, Kernel.T7_AIN149_SETTLING_US,
    Kernel.T7_AIN150_SETTLING_US, Kernel.T7_AIN151_SETTLING_US, Kernel.T7_AIN152_SETTLING_US,
    Kernel.T7_AIN153_SETTLING_US, Kernel.T7_AIN154_SETTLING_US, Kernel.T7_AIN155_SETTLING_US,
    Kernel.T7_AIN156_SETTLING_US, Kernel.T7_AIN157_SETTLING_US, Kernel.T7_AIN158_SETTLING_US,
    Kernel.T7_AIN159_SETTLING_US, Kernel.T7_AIN160_SETTLING_US, Kernel.T7_AIN161_SETTLING_US,
    Kernel.T7_AIN162_SETTLING_US, Kernel.T7_AIN163_SETTLING_US, Kernel.T7_AIN164_SETTLING_US,
    Kernel.T7_AIN165_SETTLING_US, Kernel.T7_AIN166_SETTLING_US, Kernel.T7_AIN167_SETTLING_US,
    Kernel.T7_AIN168_SETTLING_US, Kernel.T7_AIN169_SETTLING_US, Kernel.T7_AIN170_SETTLING_US,
    Kernel.T7_AIN171_SETTLING_US, Kernel.T7_AIN172_SETTLING_US, Kernel.T7_AIN173_SETTLING_US,
    Kernel.T7_AIN174_SETTLING_US, Kernel.T7_AIN175_SETTLING_US, Kernel.T7_AIN176_SETTLING_US,
    Kernel.T7_AIN177_SETTLING_US, Kernel.T7_AIN178_SETTLING_US, Kernel.T7_AIN179_SETTLING_US,
    Kernel.T7_AIN180_SETTLING_US, Kernel.T7_AIN181_SETTLING_US, Kernel.T7_AIN182_SETTLING_US,
    Kernel.T7_AIN183_SETTLING_US, Kernel.T7_AIN184_SETTLING_US, Kernel.T7_AIN185_SETTLING_US,
    Kernel.T7_AIN186_SETTLING_US, Kernel.T7_AIN187_SETTLING_US, Kernel.T7_AIN188_SETTLING_US,
    Kernel.T7_AIN189_SETTLING_US, Kernel.T7_AIN190_SETTLING_US, Kernel.T7_AIN191_SETTLING_US,
    Kernel.T7_AIN192_SETTLING_US, Kernel.T7_AIN193_SETTLING_US, Kernel.T7_AIN194_SETTLING_US,
    Kernel.T7_AIN195_SETTLING_US, Kernel.T7_AIN196_SETTLING_US, Kernel.T7_AIN197_SETTLING_US,
    Kernel.T7_AIN198_SETTLING_US, Kernel.T7_AIN199_SETTLING_US, Kernel.T7_AIN200_SETTLING_US,
    Kernel.T7_AIN201_SETTLING_US, Kernel.T7_AIN202_SETTLING_US, Kernel.T7_AIN203_SETTLING_US,
    Kernel.T7_AIN204_SETTLING_US, Kernel.T7_AIN205_SETTLING_US, Kernel.T7_AIN206_SETTLING_US,
    Kernel.T7_AIN207_SETTLING_US, Kernel.T7_AIN208_SETTLING_US, Kernel.T7_AIN209_SETTLING_US,
    Kernel.T7_AIN210_SETTLING_US, Kernel.T7_AIN211_SETTLING_US, Kernel.T7_AIN212_SETTLING_US,
    Kernel.T7_AIN213_SETTLING_US, Kernel.T7_AIN214_SETTLING_US, Kernel.T7_AIN215_SETTLING_US,
    Kernel.T7_AIN216_SETTLING_US, Kernel.T7_AIN217_SETTLING_US, Kernel.T7_AIN218_SETTLING_US,
    Kernel.T7_AIN219_SETTLING_US, Kernel.T7_AIN220_SETTLING_US, Kernel.T7_AIN221_SETTLING_US,
    Kernel.T7_AIN222_SETTLING_US, Kernel.T7_AIN223_SETTLING_US, Kernel.T7_AIN224_SETTLING_US,
    Kernel.T7_AIN225_SETTLING_US, Kernel.T7_AIN226_SETTLING_US, Kernel.T7_AIN227_SETTLING_US,
    Kernel.T7_AIN228_SETTLING_US, Kernel.T7_AIN229_SETTLING_US, Kernel.T7_AIN230_SETTLING_US,
    Kernel.T7_AIN231_SETTLING_US, Kernel.T7_AIN232_SETTLING_US, Kernel.T7_AIN233_SETTLING_US,
    Kernel.T7_AIN234_SETTLING_US, Kernel.T7_AIN235_SETTLING_US, Kernel.T7_AIN236_SETTLING_US,
    Kernel.T7_AIN237_SETTLING_US, Kernel.T7_AIN238_SETTLING_US, Kernel.T7_AIN239_SETTLING_US,
    Kernel.T7_AIN240_SETTLING_US, Kernel.T7_AIN241_SETTLING_US, Kernel.T7_AIN242_SETTLING_US,
    Kernel.T7_AIN243_SETTLING_US, Kernel.T7_AIN244_SETTLING_US, Kernel.T7_AIN245_SETTLING_US,
    Kernel.T7_AIN246_SETTLING_US, Kernel.T7_AIN247_SETTLING_US, Kernel.T7_AIN248_SETTLING_US,
    Kernel.T7_AIN249_SETTLING_US, Kernel.T7_AIN250_SETTLING_US, Kernel.T7_AIN251_SETTLING_US,
    Kernel.T7_AIN252_SETTLING_US, Kernel.T7_AIN253_SETTLING_US, Kernel.T7_AIN254_SETTLING_US,
    Kernel.T7_AIN_ALL_SETTLING_US
]


AIN_ADDRS = [
    Kernel.T7_AIN0_RANGE, Kernel.T7_AIN1_RANGE, Kernel.T7_AIN2_RANGE, Kernel.T7_AIN3_RANGE,
    Kernel.T7_AIN4_RANGE, Kernel.T7_AIN5_RANGE, Kernel.T7_AIN6_RANGE, Kernel.T7_AIN7_RANGE,
    Kernel.T7_AIN8_RANGE, Kernel.T7_AIN9_RANGE, Kernel.T7_AIN10_RANGE, Kernel.T7_AIN11_RANGE,
    Kernel.T7_AIN12_RANGE, Kernel.T7_AIN13_RANGE, Kernel.T7_AIN14_RANGE, Kernel.T7_AIN15_RANGE,
    Kernel.T7_AIN16_RANGE, Kernel.T7_AIN17_RANGE, Kernel.T7_AIN18_RANGE, Kernel.T7_AIN19_RANGE,
    Kernel.T7_AIN20_RANGE, Kernel.T7_AIN21_RANGE, Kernel.T7_AIN22_RANGE, Kernel.T7_AIN23_RANGE,
    Kernel.T7_AIN24_RANGE, Kernel.T7_AIN25_RANGE, Kernel.T7_AIN26_RANGE, Kernel.T7_AIN27_RANGE,
    Kernel.T7_AIN28_RANGE, Kernel.T7_AIN29_RANGE, Kernel.T7_AIN30_RANGE, Kernel.T7_AIN31_RANGE,
    Kernel.T7_AIN32_RANGE, Kernel.T7_AIN33_RANGE, Kernel.T7_AIN34_RANGE, Kernel.T7_AIN35_RANGE,
    Kernel.T7_AIN36_RANGE, Kernel.T7_AIN37_RANGE, Kernel.T7_AIN38_RANGE, Kernel.T7_AIN39_RANGE,
    Kernel.T7_AIN40_RANGE, Kernel.T7_AIN41_RANGE, Kernel.T7_AIN42_RANGE, Kernel.T7_AIN43_RANGE,
    Kernel.T7_AIN44_RANGE, Kernel.T7_AIN45_RANGE, Kernel.T7_AIN46_RANGE, Kernel.T7_AIN47_RANGE,
    Kernel.T7_AIN48_RANGE, Kernel.T7_AIN49_RANGE, Kernel.T7_AIN50_RANGE, Kernel.T7_AIN51_RANGE,
    Kernel.T7_AIN52_RANGE, Kernel.T7_AIN53_RANGE, Kernel.T7_AIN54_RANGE, Kernel.T7_AIN55_RANGE,
    Kernel.T7_AIN56_RANGE, Kernel.T7_AIN57_RANGE, Kernel.T7_AIN58_RANGE, Kernel.T7_AIN59_RANGE,
    Kernel.T7_AIN60_RANGE, Kernel.T7_AIN61_RANGE, Kernel.T7_AIN62_RANGE, Kernel.T7_AIN63_RANGE,
    Kernel.T7_AIN64_RANGE, Kernel.T7_AIN65_RANGE, Kernel.T7_AIN66_RANGE, Kernel.T7_AIN67_RANGE,
    Kernel.T7_AIN68_RANGE, Kernel.T7_AIN69_RANGE, Kernel.T7_AIN70_RANGE, Kernel.T7_AIN71_RANGE,
    Kernel.T7_AIN72_RANGE, Kernel.T7_AIN73_RANGE, Kernel.T7_AIN74_RANGE, Kernel.T7_AIN75_RANGE,
    Kernel.T7_AIN76_RANGE, Kernel.T7_AIN77_RANGE, Kernel.T7_AIN78_RANGE, Kernel.T7_AIN79_RANGE,
    Kernel.T7_AIN80_RANGE, Kernel.T7_AIN81_RANGE, Kernel.T7_AIN82_RANGE, Kernel.T7_AIN83_RANGE,
    Kernel.T7_AIN84_RANGE, Kernel.T7_AIN85_RANGE, Kernel.T7_AIN86_RANGE, Kernel.T7_AIN87_RANGE,
    Kernel.T7_AIN88_RANGE, Kernel.T7_AIN89_RANGE, Kernel.T7_AIN90_RANGE, Kernel.T7_AIN91_RANGE,
    Kernel.T7_AIN92_RANGE, Kernel.T7_AIN93_RANGE, Kernel.T7_AIN94_RANGE, Kernel.T7_AIN95_RANGE,
    Kernel.T7_AIN96_RANGE, Kernel.T7_AIN97_RANGE, Kernel.T7_AIN98_RANGE, Kernel.T7_AIN99_RANGE,
    Kernel.T7_AIN100_RANGE, Kernel.T7_AIN101_RANGE, Kernel.T7_AIN102_RANGE, Kernel.T7_AIN103_RANGE,
    Kernel.T7_AIN104_RANGE, Kernel.T7_AIN105_RANGE, Kernel.T7_AIN106_RANGE, Kernel.T7_AIN107_RANGE,
    Kernel.T7_AIN108_RANGE, Kernel.T7_AIN109_RANGE, Kernel.T7_AIN110_RANGE, Kernel.T7_AIN111_RANGE,
    Kernel.T7_AIN112_RANGE, Kernel.T7_AIN113_RANGE, Kernel.T7_AIN114_RANGE, Kernel.T7_AIN115_RANGE,
    Kernel.T7_AIN116_RANGE, Kernel.T7_AIN117_RANGE, Kernel.T7_AIN118_RANGE, Kernel.T7_AIN119_RANGE,
    Kernel.T7_AIN120_RANGE, Kernel.T7_AIN121_RANGE, Kernel.T7_AIN122_RANGE, Kernel.T7_AIN123_RANGE,
    Kernel.T7_AIN124_RANGE, Kernel.T7_AIN125_RANGE, Kernel.T7_AIN126_RANGE, Kernel.T7_AIN127_RANGE,
    Kernel.T7_AIN128_RANGE, Kernel.T7_AIN129_RANGE, Kernel.T7_AIN130_RANGE, Kernel.T7_AIN131_RANGE,
    Kernel.T7_AIN132_RANGE, Kernel.T7_AIN133_RANGE, Kernel.T7_AIN134_RANGE, Kernel.T7_AIN135_RANGE,
    Kernel.T7_AIN136_RANGE, Kernel.T7_AIN137_RANGE, Kernel.T7_AIN138_RANGE, Kernel.T7_AIN139_RANGE,
    Kernel.T7_AIN140_RANGE, Kernel.T7_AIN141_RANGE, Kernel.T7_AIN142_RANGE, Kernel.T7_AIN143_RANGE,
    Kernel.T7_AIN144_RANGE, Kernel.T7_AIN145_RANGE, Kernel.T7_AIN146_RANGE, Kernel.T7_AIN147_RANGE,
    Kernel.T7_AIN148_RANGE, Kernel.T7_AIN149_RANGE, Kernel.T7_AIN150_RANGE, Kernel.T7_AIN151_RANGE,
    Kernel.T7_AIN152_RANGE, Kernel.T7_AIN153_RANGE, Kernel.T7_AIN154_RANGE, Kernel.T7_AIN155_RANGE,
    Kernel.T7_AIN156_RANGE, Kernel.T7_AIN157_RANGE, Kernel.T7_AIN158_RANGE, Kernel.T7_AIN159_RANGE,
    Kernel.T7_AIN160_RANGE, Kernel.T7_AIN161_RANGE, Kernel.T7_AIN162_RANGE, Kernel.T7_AIN163_RANGE,
    Kernel.T7_AIN164_RANGE, Kernel.T7_AIN165_RANGE, Kernel.T7_AIN166_RANGE, Kernel.T7_AIN167_RANGE,
    Kernel.T7_AIN168_RANGE, Kernel.T7_AIN169_RANGE, Kernel.T7_AIN170_RANGE, Kernel.T7_AIN171_RANGE,
    Kernel.T7_AIN172_RANGE, Kernel.T7_AIN173_RANGE, Kernel.T7_AIN174_RANGE, Kernel.T7_AIN175_RANGE,
    Kernel.T7_AIN176_RANGE, Kernel.T7_AIN177_RANGE, Kernel.T7_AIN178_RANGE, Kernel.T7_AIN179_RANGE,
    Kernel.T7_AIN180_RANGE, Kernel.T7_AIN181_RANGE, Kernel.T7_AIN182_RANGE, Kernel.T7_AIN183_RANGE,
    Kernel.T7_AIN184_RANGE, Kernel.T7_AIN185_RANGE, Kernel.T7_AIN186_RANGE, Kernel.T7_AIN187_RANGE,
    Kernel.T7_AIN188_RANGE, Kernel.T7_AIN189_RANGE, Kernel.T7_AIN190_RANGE, Kernel.T7_AIN191_RANGE,
    Kernel.T7_AIN192_RANGE, Kernel.T7_AIN193_RANGE, Kernel.T7_AIN194_RANGE, Kernel.T7_AIN195_RANGE,
    Kernel.T7_AIN196_RANGE, Kernel.T7_AIN197_RANGE, Kernel.T7_AIN198_RANGE, Kernel.T7_AIN199_RANGE,
    Kernel.T7_AIN200_RANGE, Kernel.T7_AIN201_RANGE, Kernel.T7_AIN202_RANGE, Kernel.T7_AIN203_RANGE,
    Kernel.T7_AIN204_RANGE, Kernel.T7_AIN205_RANGE, Kernel.T7_AIN206_RANGE, Kernel.T7_AIN207_RANGE,
    Kernel.T7_AIN208_RANGE, Kernel.T7_AIN209_RANGE, Kernel.T7_AIN210_RANGE, Kernel.T7_AIN211_RANGE,
    Kernel.T7_AIN212_RANGE, Kernel.T7_AIN213_RANGE, Kernel.T7_AIN214_RANGE, Kernel.T7_AIN215_RANGE,
    Kernel.T7_AIN216_RANGE, Kernel.T7_AIN217_RANGE, Kernel.T7_AIN218_RANGE, Kernel.T7_AIN219_RANGE,
    Kernel.T7_AIN220_RANGE, Kernel.T7_AIN221_RANGE, Kernel.T7_AIN222_RANGE, Kernel.T7_AIN223_RANGE,
    Kernel.T7_AIN224_RANGE, Kernel.T7_AIN225_RANGE, Kernel.T7_AIN226_RANGE, Kernel.T7_AIN227_RANGE,
    Kernel.T7_AIN228_RANGE, Kernel.T7_AIN229_RANGE, Kernel.T7_AIN230_RANGE, Kernel.T7_AIN231_RANGE,
    Kernel.T7_AIN232_RANGE, Kernel.T7_AIN233_RANGE, Kernel.T7_AIN234_RANGE, Kernel.T7_AIN235_RANGE,
    Kernel.T7_AIN236_RANGE, Kernel.T7_AIN237_RANGE, Kernel.T7_AIN238_RANGE, Kernel.T7_AIN239_RANGE,
    Kernel.T7_AIN240_RANGE, Kernel.T7_AIN241_RANGE, Kernel.T7_AIN242_RANGE, Kernel.T7_AIN243_RANGE,
    Kernel.T7_AIN244_RANGE, Kernel.T7_AIN245_RANGE, Kernel.T7_AIN246_RANGE, Kernel.T7_AIN247_RANGE,
    Kernel.T7_AIN248_RANGE, Kernel.T7_AIN249_RANGE, Kernel.T7_AIN250_RANGE, Kernel.T7_AIN251_RANGE,
    Kernel.T7_AIN252_RANGE, Kernel.T7_AIN253_RANGE, Kernel.T7_AIN254_RANGE, Kernel.T7_AIN_ALL_RANGE
]

RANGE_LIST = [
    10, 1, 10.0, 1.0, 0.1, 0.01
]

DAC_ADDR_SIZE = -2
DAC_ADDR_TYPE = -3
DAC_ADDR_VALUE = -1
AIN_ADDR_SIZE = -2
AIN_ADDR_TYPE = -3
AIN_ADDR_VALUE = -1
RANGE_SIZE = -2
RANGE_TYPE = -3
RANGE_VALUE = -1
"""
/**********************************************************************************************************************/
/****************************************DIRECT ACCESS TO DEVICE FUNCTION**********************************************/
/**********************************************************************************************************************/
"""


def ld_dio_update_config(handle, dio_dir, dio_state):
    """

    :param handle:
    :param dio_dir:
    :param dio_state:
    :return:
    """
    fio_state_register = ljm.eReadAddress(handle, Kernel.T7_FIO_STATE, Kernel.T7_FIO_STATE_T)
    fio_dir_register = ljm.eReadAddress(handle, Kernel.T7_FIO_DIR, Kernel.T7_FIO_DIR_T)
    ljm.eWriteAddress(handle, Kernel.T7_FIO_DIR, Kernel.T7_FIO_DIR_T, fio_dir_register | dio_dir)
    ljm.eWriteAddress(handle, Kernel.T7_FIO_STATE, Kernel.T7_FIO_STATE_T, fio_state_register | dio_state)
    return


def ld_dio_erase_config(handle, dio_dir, dio_state):
    """

    :param handle:
    :param dio_dir:
    :param dio_state:
    :return:
    """
    ljm.eWriteAddress(handle, Kernel.T7_FIO_DIR, Kernel.T7_FIO_DIR_T, dio_dir)
    ljm.eWriteAddress(handle, Kernel.T7_FIO_STATE, Kernel.T7_FIO_STATE_T, dio_state)
    return


def ld_dac_alter_config(handle, dac_addr, value_list):
    valid_addr = dac_addr_validator(dac_addr)
    valid_voltage = dac_output_voltage_validator(value_list)
    if 1 == valid_addr:
        if 1 == valid_voltage:
            if len(value_list) == len(dac_addr):
                for voltage, addr in zip(value_list, dac_addr):
                    ljm.eWriteAddress(handle, addr, Kernel.T7_DAC_T, voltage)
            else:
                print(
                    "\
                    Unable to configure analog output voltage due to voltage array size less than address array size.\
                    "
                )
                return -1
        elif 0 == valid_voltage:
            for addr in dac_addr:
                ljm.eWriteAddress(handle, addr, Kernel.T7_DAC_T, value_list)
        else:
            voltage_error(valid_voltage, value_list)
            return -1
    elif 2 == valid_addr:
        if 0 == valid_voltage:
            ljm.eWriteAddress(handle, dac_addr, Kernel.T7_DAC_T, value_list)
        elif 1 == valid_voltage:
            print("Well it is correct, " +
                  "but configuring multiple voltage for a single analog address doesn't make sense, isn't it?")
            print("ranges:" + str(value_list))
            print("address:" + str(dac_addr))
            return -1
        else:
            voltage_error(valid_voltage, value_list)
            return -1
    else:
        dac_addr_error(valid_addr, dac_addr)
        return -1
    return 0


def aio_alter_resolution_config(handle, addr_list, res_list):
    valid_addr = res_validator(addr_list)
    valid_res = res_validator(res_list)
    return


def aio_alter_settling_time_config(handle, addr_list, settling_time_list):
    valid_addr = settling_addr_validator(addr_list)
    valid_res = settling_time_validator(settling_time_list)
    return


def ld_aio_alter_range_config(handle, addr_list, range_list):
    """
        function to update range(s) of analog input
    :param handle:
    :param range_list:
    :param addr_list:
    :return: error: -1 success: 0
    """
    valid_addr = ain_addr_validator(addr_list)
    valid_range = range_validator(range_list)
    if 1 == valid_addr:
        if 1 == valid_range:
            if len(range_list) == len(addr_list):
                for range_v, ain_addr in zip(range_list, addr_list):
                    ljm.eWriteAddress(handle, ain_addr, Kernel.T7_AIN_RANGE_T, range_v)
            else:
                print(
                    "\
                    Unable to configure analog resolution due to resolutions array size less than address array size.\
                    "
                )
                return -1
        elif 2 == valid_range:
            for ain_addr in addr_list:
                ljm.eWriteAddress(handle, ain_addr, Kernel.T7_AIN_RANGE_T, range_list)
        elif 3 == valid_range:
            for ain_addr in addr_list:
                ljm.eWriteAddress(handle, ain_addr, Kernel.T7_AIN_RANGE_T, range_list)
        else:
            range_error(valid_range, range_list)
            return -1
    elif 2 == valid_addr:
        if 2 == valid_range:
            ljm.eWriteAddress(handle, addr_list, Kernel.T7_AIN_RANGE_T, range_list)
        elif 3 == valid_range:
            ljm.eWriteAddress(handle, addr_list, Kernel.T7_AIN_RANGE_T, range_list)
        elif 1 == valid_range:
            print("Well it is correct, " +
                  "but configuring multiple range for a single analog address doesn't make sense, isn't it?")
            print("ranges:" + str(range_list))
            print("address:" + str(addr_list))
            return -1
        else:
            range_error(valid_range, range_list)
    else:
        ain_addr_error(valid_addr, addr_list)
        return -1
    return 0


"""
/**********************************************************************************************************************/
/**************************************************CONFIG FUNCTION*****************************************************/
/**********************************************************************************************************************/
"""


def ld_dio_config(handles, dio_dir=None, dio_state=None, update_dio=0):
    """

    :param handles:
    :param dio_dir:
    :param dio_state:
    :param update_dio:
    :return:
    """
    if dio_dir is not None and dio_state is not None:
        if dio_dir > 255:
            dio_dir = 255
        if dio_state > 255:
            dio_state = 255
        if dio_state - dio_dir > dio_state:
            dio_state = dio_state - dio_dir
        for handle in handles:
            if 1 == update_dio:
                try:
                    ld_dio_update_config(handle, dio_dir, dio_state)
                except ljm.ljm.LJMError:
                    print("Error unable to communicate with device " + str(ljm.getHandleInfo(handle)))
                    print("Leaving unconfigured.")
                    handles.remove(handle)
                    print("Device removed from the list of devices")
            else:
                try:
                    ld_dio_erase_config(handle, dio_dir, dio_state)
                except ljm.ljm.LJMError:
                    print("Error unable to communicate with device " + str(ljm.getHandleInfo(handle)))
                    print("Leaving unconfigured.")
                    handles.remove(handle)
                    print("Device removed from the list of devices")
    return 0


def ld_settling_config(handles, addr_list, settling_time):
    for handle in handles:
        try:
            if 0 > aio_alter_resolution_config(handle, addr_list, settling_time):
                print("Error occurred during configuration of device " + str(ljm.getHandleInfo(handle)))
                return -1
        except ljm.ljm.LJMError:
            print("Error unable to communicate with device " + str(ljm.getHandleInfo(handle)))
            print("Leaving unconfigured.")
            handles.remove(handle)
            print("Device removed from the list of devices")
    return 0


def ld_resolution_config(handles, addr_list, res_list):
    for handle in handles:
        try:
            if 0 > aio_alter_resolution_config(handle, addr_list, res_list):
                print("Error occurred during configuration of device " + str(ljm.getHandleInfo(handle)))
                return -1
        except ljm.ljm.LJMError:
            print("Error unable to communicate with device " + str(ljm.getHandleInfo(handle)))
            print("Leaving unconfigured.")
            handles.remove(handle)
            print("Device removed from the list of devices")
    return 0


def ld_ain_config(handles, analog_addr, aio_dir=0, ain_range=None, dac_values=None):
    """

    :param handles:
    :param analog_addr:
    :param aio_dir:
    :param ain_range:
    :param dac_values:
    :return:
    """
    if 1 == aio_dir:
        print("\tConfiguring analog input")
        if handles is not None and analog_addr is not None and ain_range is not None:
            for handle in handles:
                try:
                    if 0 > ld_aio_alter_range_config(handle, analog_addr, ain_range):
                        print("Error occurred during configuration of device " + str(ljm.getHandleInfo(handle)))
                        return -1
                except ljm.ljm.LJMError:
                    print("Error unable to communicate with device " + str(ljm.getHandleInfo(handle)))
                    print("Leaving unconfigured.")
                    handles.remove(handle)
                    print("Device removed from the list of devices")
        else:
            print("ERROR: Leaving analog input to current labjack configuration")
            return -1
    elif 0 == aio_dir:
        print("\tConfiguring analog output")
        if handles is not None and analog_addr is not None and dac_values is not None:
            for handle in handles:
                try:
                    if 0 > ld_dac_alter_config(handle, analog_addr, dac_values):
                        print("Error occurred during configuration of device " + str(ljm.getHandleInfo(handle)))
                        return -1
                except ljm.ljm.LJMError:
                    print("Error unable to communicate with device " + str(ljm.getHandleInfo(handle)))
                    print("Leaving unconfigured.")
                    handles.remove(handle)
                    print("Device removed from the list of devices")
        else:
            print("ERROR: Leaving analog output to current labjack configuration")
            return -1
    return 0


"""
/**********************************************************************************************************************/
/************************************************VALIDATION FUNCTION***************************************************/
/**********************************************************************************************************************/
"""


def ain_addr_validator(addr_list, display=0):
    ain_addr = [
        Kernel.T7_AIN0_RANGE, Kernel.T7_AIN1_RANGE, Kernel.T7_AIN2_RANGE, Kernel.T7_AIN3_RANGE,
        Kernel.T7_AIN4_RANGE, Kernel.T7_AIN5_RANGE, Kernel.T7_AIN6_RANGE, Kernel.T7_AIN7_RANGE,
        Kernel.T7_AIN8_RANGE, Kernel.T7_AIN9_RANGE, Kernel.T7_AIN10_RANGE, Kernel.T7_AIN11_RANGE,
        Kernel.T7_AIN12_RANGE, Kernel.T7_AIN13_RANGE, Kernel.T7_AIN14_RANGE, Kernel.T7_AIN15_RANGE,
        Kernel.T7_AIN16_RANGE, Kernel.T7_AIN17_RANGE, Kernel.T7_AIN18_RANGE, Kernel.T7_AIN19_RANGE,
        Kernel.T7_AIN20_RANGE, Kernel.T7_AIN21_RANGE, Kernel.T7_AIN22_RANGE, Kernel.T7_AIN23_RANGE,
        Kernel.T7_AIN24_RANGE, Kernel.T7_AIN25_RANGE, Kernel.T7_AIN26_RANGE, Kernel.T7_AIN27_RANGE,
        Kernel.T7_AIN28_RANGE, Kernel.T7_AIN29_RANGE, Kernel.T7_AIN30_RANGE, Kernel.T7_AIN31_RANGE,
        Kernel.T7_AIN32_RANGE, Kernel.T7_AIN33_RANGE, Kernel.T7_AIN34_RANGE, Kernel.T7_AIN35_RANGE,
        Kernel.T7_AIN36_RANGE, Kernel.T7_AIN37_RANGE, Kernel.T7_AIN38_RANGE, Kernel.T7_AIN39_RANGE,
        Kernel.T7_AIN40_RANGE, Kernel.T7_AIN41_RANGE, Kernel.T7_AIN42_RANGE, Kernel.T7_AIN43_RANGE,
        Kernel.T7_AIN44_RANGE, Kernel.T7_AIN45_RANGE, Kernel.T7_AIN46_RANGE, Kernel.T7_AIN47_RANGE,
        Kernel.T7_AIN48_RANGE, Kernel.T7_AIN49_RANGE, Kernel.T7_AIN50_RANGE, Kernel.T7_AIN51_RANGE,
        Kernel.T7_AIN52_RANGE, Kernel.T7_AIN53_RANGE, Kernel.T7_AIN54_RANGE, Kernel.T7_AIN55_RANGE,
        Kernel.T7_AIN56_RANGE, Kernel.T7_AIN57_RANGE, Kernel.T7_AIN58_RANGE, Kernel.T7_AIN59_RANGE,
        Kernel.T7_AIN60_RANGE, Kernel.T7_AIN61_RANGE, Kernel.T7_AIN62_RANGE, Kernel.T7_AIN63_RANGE,
        Kernel.T7_AIN64_RANGE, Kernel.T7_AIN65_RANGE, Kernel.T7_AIN66_RANGE, Kernel.T7_AIN67_RANGE,
        Kernel.T7_AIN68_RANGE, Kernel.T7_AIN69_RANGE, Kernel.T7_AIN70_RANGE, Kernel.T7_AIN71_RANGE,
        Kernel.T7_AIN72_RANGE, Kernel.T7_AIN73_RANGE, Kernel.T7_AIN74_RANGE, Kernel.T7_AIN75_RANGE,
        Kernel.T7_AIN76_RANGE, Kernel.T7_AIN77_RANGE, Kernel.T7_AIN78_RANGE, Kernel.T7_AIN79_RANGE,
        Kernel.T7_AIN80_RANGE, Kernel.T7_AIN81_RANGE, Kernel.T7_AIN82_RANGE, Kernel.T7_AIN83_RANGE,
        Kernel.T7_AIN84_RANGE, Kernel.T7_AIN85_RANGE, Kernel.T7_AIN86_RANGE, Kernel.T7_AIN87_RANGE,
        Kernel.T7_AIN88_RANGE, Kernel.T7_AIN89_RANGE, Kernel.T7_AIN90_RANGE, Kernel.T7_AIN91_RANGE,
        Kernel.T7_AIN92_RANGE, Kernel.T7_AIN93_RANGE, Kernel.T7_AIN94_RANGE, Kernel.T7_AIN95_RANGE,
        Kernel.T7_AIN96_RANGE, Kernel.T7_AIN97_RANGE, Kernel.T7_AIN98_RANGE, Kernel.T7_AIN99_RANGE,
        Kernel.T7_AIN100_RANGE, Kernel.T7_AIN101_RANGE, Kernel.T7_AIN102_RANGE, Kernel.T7_AIN103_RANGE,
        Kernel.T7_AIN104_RANGE, Kernel.T7_AIN105_RANGE, Kernel.T7_AIN106_RANGE, Kernel.T7_AIN107_RANGE,
        Kernel.T7_AIN108_RANGE, Kernel.T7_AIN109_RANGE, Kernel.T7_AIN110_RANGE, Kernel.T7_AIN111_RANGE,
        Kernel.T7_AIN112_RANGE, Kernel.T7_AIN113_RANGE, Kernel.T7_AIN114_RANGE, Kernel.T7_AIN115_RANGE,
        Kernel.T7_AIN116_RANGE, Kernel.T7_AIN117_RANGE, Kernel.T7_AIN118_RANGE, Kernel.T7_AIN119_RANGE,
        Kernel.T7_AIN120_RANGE, Kernel.T7_AIN121_RANGE, Kernel.T7_AIN122_RANGE, Kernel.T7_AIN123_RANGE,
        Kernel.T7_AIN124_RANGE, Kernel.T7_AIN125_RANGE, Kernel.T7_AIN126_RANGE, Kernel.T7_AIN127_RANGE,
        Kernel.T7_AIN128_RANGE, Kernel.T7_AIN129_RANGE, Kernel.T7_AIN130_RANGE, Kernel.T7_AIN131_RANGE,
        Kernel.T7_AIN132_RANGE, Kernel.T7_AIN133_RANGE, Kernel.T7_AIN134_RANGE, Kernel.T7_AIN135_RANGE,
        Kernel.T7_AIN136_RANGE, Kernel.T7_AIN137_RANGE, Kernel.T7_AIN138_RANGE, Kernel.T7_AIN139_RANGE,
        Kernel.T7_AIN140_RANGE, Kernel.T7_AIN141_RANGE, Kernel.T7_AIN142_RANGE, Kernel.T7_AIN143_RANGE,
        Kernel.T7_AIN144_RANGE, Kernel.T7_AIN145_RANGE, Kernel.T7_AIN146_RANGE, Kernel.T7_AIN147_RANGE,
        Kernel.T7_AIN148_RANGE, Kernel.T7_AIN149_RANGE, Kernel.T7_AIN150_RANGE, Kernel.T7_AIN151_RANGE,
        Kernel.T7_AIN152_RANGE, Kernel.T7_AIN153_RANGE, Kernel.T7_AIN154_RANGE, Kernel.T7_AIN155_RANGE,
        Kernel.T7_AIN156_RANGE, Kernel.T7_AIN157_RANGE, Kernel.T7_AIN158_RANGE, Kernel.T7_AIN159_RANGE,
        Kernel.T7_AIN160_RANGE, Kernel.T7_AIN161_RANGE, Kernel.T7_AIN162_RANGE, Kernel.T7_AIN163_RANGE,
        Kernel.T7_AIN164_RANGE, Kernel.T7_AIN165_RANGE, Kernel.T7_AIN166_RANGE, Kernel.T7_AIN167_RANGE,
        Kernel.T7_AIN168_RANGE, Kernel.T7_AIN169_RANGE, Kernel.T7_AIN170_RANGE, Kernel.T7_AIN171_RANGE,
        Kernel.T7_AIN172_RANGE, Kernel.T7_AIN173_RANGE, Kernel.T7_AIN174_RANGE, Kernel.T7_AIN175_RANGE,
        Kernel.T7_AIN176_RANGE, Kernel.T7_AIN177_RANGE, Kernel.T7_AIN178_RANGE, Kernel.T7_AIN179_RANGE,
        Kernel.T7_AIN180_RANGE, Kernel.T7_AIN181_RANGE, Kernel.T7_AIN182_RANGE, Kernel.T7_AIN183_RANGE,
        Kernel.T7_AIN184_RANGE, Kernel.T7_AIN185_RANGE, Kernel.T7_AIN186_RANGE, Kernel.T7_AIN187_RANGE,
        Kernel.T7_AIN188_RANGE, Kernel.T7_AIN189_RANGE, Kernel.T7_AIN190_RANGE, Kernel.T7_AIN191_RANGE,
        Kernel.T7_AIN192_RANGE, Kernel.T7_AIN193_RANGE, Kernel.T7_AIN194_RANGE, Kernel.T7_AIN195_RANGE,
        Kernel.T7_AIN196_RANGE, Kernel.T7_AIN197_RANGE, Kernel.T7_AIN198_RANGE, Kernel.T7_AIN199_RANGE,
        Kernel.T7_AIN200_RANGE, Kernel.T7_AIN201_RANGE, Kernel.T7_AIN202_RANGE, Kernel.T7_AIN203_RANGE,
        Kernel.T7_AIN204_RANGE, Kernel.T7_AIN205_RANGE, Kernel.T7_AIN206_RANGE, Kernel.T7_AIN207_RANGE,
        Kernel.T7_AIN208_RANGE, Kernel.T7_AIN209_RANGE, Kernel.T7_AIN210_RANGE, Kernel.T7_AIN211_RANGE,
        Kernel.T7_AIN212_RANGE, Kernel.T7_AIN213_RANGE, Kernel.T7_AIN214_RANGE, Kernel.T7_AIN215_RANGE,
        Kernel.T7_AIN216_RANGE, Kernel.T7_AIN217_RANGE, Kernel.T7_AIN218_RANGE, Kernel.T7_AIN219_RANGE,
        Kernel.T7_AIN220_RANGE, Kernel.T7_AIN221_RANGE, Kernel.T7_AIN222_RANGE, Kernel.T7_AIN223_RANGE,
        Kernel.T7_AIN224_RANGE, Kernel.T7_AIN225_RANGE, Kernel.T7_AIN226_RANGE, Kernel.T7_AIN227_RANGE,
        Kernel.T7_AIN228_RANGE, Kernel.T7_AIN229_RANGE, Kernel.T7_AIN230_RANGE, Kernel.T7_AIN231_RANGE,
        Kernel.T7_AIN232_RANGE, Kernel.T7_AIN233_RANGE, Kernel.T7_AIN234_RANGE, Kernel.T7_AIN235_RANGE,
        Kernel.T7_AIN236_RANGE, Kernel.T7_AIN237_RANGE, Kernel.T7_AIN238_RANGE, Kernel.T7_AIN239_RANGE,
        Kernel.T7_AIN240_RANGE, Kernel.T7_AIN241_RANGE, Kernel.T7_AIN242_RANGE, Kernel.T7_AIN243_RANGE,
        Kernel.T7_AIN244_RANGE, Kernel.T7_AIN245_RANGE, Kernel.T7_AIN246_RANGE, Kernel.T7_AIN247_RANGE,
        Kernel.T7_AIN248_RANGE, Kernel.T7_AIN249_RANGE, Kernel.T7_AIN250_RANGE, Kernel.T7_AIN251_RANGE,
        Kernel.T7_AIN252_RANGE, Kernel.T7_AIN253_RANGE, Kernel.T7_AIN254_RANGE
    ]
    if type(addr_list) == type([]):
        if 0 != len(addr_list):
            for addr in addr_list:
                try:
                    test = ain_addr.index(addr)
                except ValueError:
                    if display:
                        print("Address: " + str(addr) + " is an invalid input analog address.")
                    return -1
            return 1
        else:
            return -2
    elif isinstance(addr_list, int):
        try:
            test = ain_addr.index(addr_list)
        except ValueError:
            if display:
                print("Address: " + str(addr_list) + " is an invalid input analog address.")
            return -1
        return 2
    else:
        if display:
            print("Found " + str(type(addr_list)) + " instead of " + str(type([])) + " or " + str(int))
        return -3


def res_addr_validator(addr_list, display=0):
    res_addr = [
        Kernel.T7_AIN0_RESOLUTION_INDEX, Kernel.T7_AIN1_RESOLUTION_INDEX, Kernel.T7_AIN2_RESOLUTION_INDEX,
        Kernel.T7_AIN3_RESOLUTION_INDEX, Kernel.T7_AIN4_RESOLUTION_INDEX, Kernel.T7_AIN5_RESOLUTION_INDEX,
        Kernel.T7_AIN6_RESOLUTION_INDEX, Kernel.T7_AIN7_RESOLUTION_INDEX, Kernel.T7_AIN8_RESOLUTION_INDEX,
        Kernel.T7_AIN9_RESOLUTION_INDEX, Kernel.T7_AIN10_RESOLUTION_INDEX, Kernel.T7_AIN11_RESOLUTION_INDEX,
        Kernel.T7_AIN12_RESOLUTION_INDEX, Kernel.T7_AIN13_RESOLUTION_INDEX, Kernel.T7_AIN14_RESOLUTION_INDEX,
        Kernel.T7_AIN15_RESOLUTION_INDEX, Kernel.T7_AIN16_RESOLUTION_INDEX, Kernel.T7_AIN17_RESOLUTION_INDEX,
        Kernel.T7_AIN18_RESOLUTION_INDEX, Kernel.T7_AIN19_RESOLUTION_INDEX, Kernel.T7_AIN20_RESOLUTION_INDEX,
        Kernel.T7_AIN21_RESOLUTION_INDEX, Kernel.T7_AIN22_RESOLUTION_INDEX, Kernel.T7_AIN23_RESOLUTION_INDEX,
        Kernel.T7_AIN24_RESOLUTION_INDEX, Kernel.T7_AIN25_RESOLUTION_INDEX, Kernel.T7_AIN26_RESOLUTION_INDEX,
        Kernel.T7_AIN27_RESOLUTION_INDEX, Kernel.T7_AIN28_RESOLUTION_INDEX, Kernel.T7_AIN29_RESOLUTION_INDEX,
        Kernel.T7_AIN30_RESOLUTION_INDEX, Kernel.T7_AIN31_RESOLUTION_INDEX, Kernel.T7_AIN32_RESOLUTION_INDEX,
        Kernel.T7_AIN33_RESOLUTION_INDEX, Kernel.T7_AIN34_RESOLUTION_INDEX, Kernel.T7_AIN35_RESOLUTION_INDEX,
        Kernel.T7_AIN36_RESOLUTION_INDEX, Kernel.T7_AIN37_RESOLUTION_INDEX, Kernel.T7_AIN38_RESOLUTION_INDEX,
        Kernel.T7_AIN39_RESOLUTION_INDEX, Kernel.T7_AIN40_RESOLUTION_INDEX, Kernel.T7_AIN41_RESOLUTION_INDEX,
        Kernel.T7_AIN42_RESOLUTION_INDEX, Kernel.T7_AIN43_RESOLUTION_INDEX, Kernel.T7_AIN44_RESOLUTION_INDEX,
        Kernel.T7_AIN45_RESOLUTION_INDEX, Kernel.T7_AIN46_RESOLUTION_INDEX, Kernel.T7_AIN47_RESOLUTION_INDEX,
        Kernel.T7_AIN48_RESOLUTION_INDEX, Kernel.T7_AIN49_RESOLUTION_INDEX, Kernel.T7_AIN50_RESOLUTION_INDEX,
        Kernel.T7_AIN51_RESOLUTION_INDEX, Kernel.T7_AIN52_RESOLUTION_INDEX, Kernel.T7_AIN53_RESOLUTION_INDEX,
        Kernel.T7_AIN54_RESOLUTION_INDEX, Kernel.T7_AIN55_RESOLUTION_INDEX, Kernel.T7_AIN56_RESOLUTION_INDEX,
        Kernel.T7_AIN57_RESOLUTION_INDEX, Kernel.T7_AIN58_RESOLUTION_INDEX, Kernel.T7_AIN59_RESOLUTION_INDEX,
        Kernel.T7_AIN60_RESOLUTION_INDEX, Kernel.T7_AIN61_RESOLUTION_INDEX, Kernel.T7_AIN62_RESOLUTION_INDEX,
        Kernel.T7_AIN63_RESOLUTION_INDEX, Kernel.T7_AIN64_RESOLUTION_INDEX, Kernel.T7_AIN65_RESOLUTION_INDEX,
        Kernel.T7_AIN66_RESOLUTION_INDEX, Kernel.T7_AIN67_RESOLUTION_INDEX, Kernel.T7_AIN68_RESOLUTION_INDEX,
        Kernel.T7_AIN69_RESOLUTION_INDEX, Kernel.T7_AIN70_RESOLUTION_INDEX, Kernel.T7_AIN71_RESOLUTION_INDEX,
        Kernel.T7_AIN72_RESOLUTION_INDEX, Kernel.T7_AIN73_RESOLUTION_INDEX, Kernel.T7_AIN74_RESOLUTION_INDEX,
        Kernel.T7_AIN75_RESOLUTION_INDEX, Kernel.T7_AIN76_RESOLUTION_INDEX, Kernel.T7_AIN77_RESOLUTION_INDEX,
        Kernel.T7_AIN78_RESOLUTION_INDEX, Kernel.T7_AIN79_RESOLUTION_INDEX, Kernel.T7_AIN80_RESOLUTION_INDEX,
        Kernel.T7_AIN81_RESOLUTION_INDEX, Kernel.T7_AIN82_RESOLUTION_INDEX, Kernel.T7_AIN83_RESOLUTION_INDEX,
        Kernel.T7_AIN84_RESOLUTION_INDEX, Kernel.T7_AIN85_RESOLUTION_INDEX, Kernel.T7_AIN86_RESOLUTION_INDEX,
        Kernel.T7_AIN87_RESOLUTION_INDEX, Kernel.T7_AIN88_RESOLUTION_INDEX, Kernel.T7_AIN89_RESOLUTION_INDEX,
        Kernel.T7_AIN90_RESOLUTION_INDEX, Kernel.T7_AIN91_RESOLUTION_INDEX, Kernel.T7_AIN92_RESOLUTION_INDEX,
        Kernel.T7_AIN93_RESOLUTION_INDEX, Kernel.T7_AIN94_RESOLUTION_INDEX, Kernel.T7_AIN95_RESOLUTION_INDEX,
        Kernel.T7_AIN96_RESOLUTION_INDEX, Kernel.T7_AIN97_RESOLUTION_INDEX, Kernel.T7_AIN98_RESOLUTION_INDEX,
        Kernel.T7_AIN99_RESOLUTION_INDEX, Kernel.T7_AIN100_RESOLUTION_INDEX, Kernel.T7_AIN101_RESOLUTION_INDEX,
        Kernel.T7_AIN102_RESOLUTION_INDEX, Kernel.T7_AIN103_RESOLUTION_INDEX, Kernel.T7_AIN104_RESOLUTION_INDEX,
        Kernel.T7_AIN105_RESOLUTION_INDEX, Kernel.T7_AIN106_RESOLUTION_INDEX, Kernel.T7_AIN107_RESOLUTION_INDEX,
        Kernel.T7_AIN108_RESOLUTION_INDEX, Kernel.T7_AIN109_RESOLUTION_INDEX, Kernel.T7_AIN110_RESOLUTION_INDEX,
        Kernel.T7_AIN111_RESOLUTION_INDEX, Kernel.T7_AIN112_RESOLUTION_INDEX, Kernel.T7_AIN113_RESOLUTION_INDEX,
        Kernel.T7_AIN114_RESOLUTION_INDEX, Kernel.T7_AIN115_RESOLUTION_INDEX, Kernel.T7_AIN116_RESOLUTION_INDEX,
        Kernel.T7_AIN117_RESOLUTION_INDEX, Kernel.T7_AIN118_RESOLUTION_INDEX, Kernel.T7_AIN119_RESOLUTION_INDEX,
        Kernel.T7_AIN120_RESOLUTION_INDEX, Kernel.T7_AIN121_RESOLUTION_INDEX, Kernel.T7_AIN122_RESOLUTION_INDEX,
        Kernel.T7_AIN123_RESOLUTION_INDEX, Kernel.T7_AIN124_RESOLUTION_INDEX, Kernel.T7_AIN125_RESOLUTION_INDEX,
        Kernel.T7_AIN126_RESOLUTION_INDEX, Kernel.T7_AIN127_RESOLUTION_INDEX, Kernel.T7_AIN128_RESOLUTION_INDEX,
        Kernel.T7_AIN129_RESOLUTION_INDEX, Kernel.T7_AIN130_RESOLUTION_INDEX, Kernel.T7_AIN131_RESOLUTION_INDEX,
        Kernel.T7_AIN132_RESOLUTION_INDEX, Kernel.T7_AIN133_RESOLUTION_INDEX, Kernel.T7_AIN134_RESOLUTION_INDEX,
        Kernel.T7_AIN135_RESOLUTION_INDEX, Kernel.T7_AIN136_RESOLUTION_INDEX, Kernel.T7_AIN137_RESOLUTION_INDEX,
        Kernel.T7_AIN138_RESOLUTION_INDEX, Kernel.T7_AIN139_RESOLUTION_INDEX, Kernel.T7_AIN140_RESOLUTION_INDEX,
        Kernel.T7_AIN141_RESOLUTION_INDEX, Kernel.T7_AIN142_RESOLUTION_INDEX, Kernel.T7_AIN143_RESOLUTION_INDEX,
        Kernel.T7_AIN144_RESOLUTION_INDEX, Kernel.T7_AIN145_RESOLUTION_INDEX, Kernel.T7_AIN146_RESOLUTION_INDEX,
        Kernel.T7_AIN147_RESOLUTION_INDEX, Kernel.T7_AIN148_RESOLUTION_INDEX, Kernel.T7_AIN149_RESOLUTION_INDEX,
        Kernel.T7_AIN150_RESOLUTION_INDEX, Kernel.T7_AIN151_RESOLUTION_INDEX, Kernel.T7_AIN152_RESOLUTION_INDEX,
        Kernel.T7_AIN153_RESOLUTION_INDEX, Kernel.T7_AIN154_RESOLUTION_INDEX, Kernel.T7_AIN155_RESOLUTION_INDEX,
        Kernel.T7_AIN156_RESOLUTION_INDEX, Kernel.T7_AIN157_RESOLUTION_INDEX, Kernel.T7_AIN158_RESOLUTION_INDEX,
        Kernel.T7_AIN159_RESOLUTION_INDEX, Kernel.T7_AIN160_RESOLUTION_INDEX, Kernel.T7_AIN161_RESOLUTION_INDEX,
        Kernel.T7_AIN162_RESOLUTION_INDEX, Kernel.T7_AIN163_RESOLUTION_INDEX, Kernel.T7_AIN164_RESOLUTION_INDEX,
        Kernel.T7_AIN165_RESOLUTION_INDEX, Kernel.T7_AIN166_RESOLUTION_INDEX, Kernel.T7_AIN167_RESOLUTION_INDEX,
        Kernel.T7_AIN168_RESOLUTION_INDEX, Kernel.T7_AIN169_RESOLUTION_INDEX, Kernel.T7_AIN170_RESOLUTION_INDEX,
        Kernel.T7_AIN171_RESOLUTION_INDEX, Kernel.T7_AIN172_RESOLUTION_INDEX, Kernel.T7_AIN173_RESOLUTION_INDEX,
        Kernel.T7_AIN174_RESOLUTION_INDEX, Kernel.T7_AIN175_RESOLUTION_INDEX, Kernel.T7_AIN176_RESOLUTION_INDEX,
        Kernel.T7_AIN177_RESOLUTION_INDEX, Kernel.T7_AIN178_RESOLUTION_INDEX, Kernel.T7_AIN179_RESOLUTION_INDEX,
        Kernel.T7_AIN180_RESOLUTION_INDEX, Kernel.T7_AIN181_RESOLUTION_INDEX, Kernel.T7_AIN182_RESOLUTION_INDEX,
        Kernel.T7_AIN183_RESOLUTION_INDEX, Kernel.T7_AIN184_RESOLUTION_INDEX, Kernel.T7_AIN185_RESOLUTION_INDEX,
        Kernel.T7_AIN186_RESOLUTION_INDEX, Kernel.T7_AIN187_RESOLUTION_INDEX, Kernel.T7_AIN188_RESOLUTION_INDEX,
        Kernel.T7_AIN189_RESOLUTION_INDEX, Kernel.T7_AIN190_RESOLUTION_INDEX, Kernel.T7_AIN191_RESOLUTION_INDEX,
        Kernel.T7_AIN192_RESOLUTION_INDEX, Kernel.T7_AIN193_RESOLUTION_INDEX, Kernel.T7_AIN194_RESOLUTION_INDEX,
        Kernel.T7_AIN195_RESOLUTION_INDEX, Kernel.T7_AIN196_RESOLUTION_INDEX, Kernel.T7_AIN197_RESOLUTION_INDEX,
        Kernel.T7_AIN198_RESOLUTION_INDEX, Kernel.T7_AIN199_RESOLUTION_INDEX, Kernel.T7_AIN200_RESOLUTION_INDEX,
        Kernel.T7_AIN201_RESOLUTION_INDEX, Kernel.T7_AIN202_RESOLUTION_INDEX, Kernel.T7_AIN203_RESOLUTION_INDEX,
        Kernel.T7_AIN204_RESOLUTION_INDEX, Kernel.T7_AIN205_RESOLUTION_INDEX, Kernel.T7_AIN206_RESOLUTION_INDEX,
        Kernel.T7_AIN207_RESOLUTION_INDEX, Kernel.T7_AIN208_RESOLUTION_INDEX, Kernel.T7_AIN209_RESOLUTION_INDEX,
        Kernel.T7_AIN210_RESOLUTION_INDEX, Kernel.T7_AIN211_RESOLUTION_INDEX, Kernel.T7_AIN212_RESOLUTION_INDEX,
        Kernel.T7_AIN213_RESOLUTION_INDEX, Kernel.T7_AIN214_RESOLUTION_INDEX, Kernel.T7_AIN215_RESOLUTION_INDEX,
        Kernel.T7_AIN216_RESOLUTION_INDEX, Kernel.T7_AIN217_RESOLUTION_INDEX, Kernel.T7_AIN218_RESOLUTION_INDEX,
        Kernel.T7_AIN219_RESOLUTION_INDEX, Kernel.T7_AIN220_RESOLUTION_INDEX, Kernel.T7_AIN221_RESOLUTION_INDEX,
        Kernel.T7_AIN222_RESOLUTION_INDEX, Kernel.T7_AIN223_RESOLUTION_INDEX, Kernel.T7_AIN224_RESOLUTION_INDEX,
        Kernel.T7_AIN225_RESOLUTION_INDEX, Kernel.T7_AIN226_RESOLUTION_INDEX, Kernel.T7_AIN227_RESOLUTION_INDEX,
        Kernel.T7_AIN228_RESOLUTION_INDEX, Kernel.T7_AIN229_RESOLUTION_INDEX, Kernel.T7_AIN230_RESOLUTION_INDEX,
        Kernel.T7_AIN231_RESOLUTION_INDEX, Kernel.T7_AIN232_RESOLUTION_INDEX, Kernel.T7_AIN233_RESOLUTION_INDEX,
        Kernel.T7_AIN234_RESOLUTION_INDEX, Kernel.T7_AIN235_RESOLUTION_INDEX, Kernel.T7_AIN236_RESOLUTION_INDEX,
        Kernel.T7_AIN237_RESOLUTION_INDEX, Kernel.T7_AIN238_RESOLUTION_INDEX, Kernel.T7_AIN239_RESOLUTION_INDEX,
        Kernel.T7_AIN240_RESOLUTION_INDEX, Kernel.T7_AIN241_RESOLUTION_INDEX, Kernel.T7_AIN242_RESOLUTION_INDEX,
        Kernel.T7_AIN243_RESOLUTION_INDEX, Kernel.T7_AIN244_RESOLUTION_INDEX, Kernel.T7_AIN245_RESOLUTION_INDEX,
        Kernel.T7_AIN246_RESOLUTION_INDEX, Kernel.T7_AIN247_RESOLUTION_INDEX, Kernel.T7_AIN248_RESOLUTION_INDEX,
        Kernel.T7_AIN249_RESOLUTION_INDEX, Kernel.T7_AIN250_RESOLUTION_INDEX, Kernel.T7_AIN251_RESOLUTION_INDEX,
        Kernel.T7_AIN252_RESOLUTION_INDEX, Kernel.T7_AIN253_RESOLUTION_INDEX, Kernel.T7_AIN254_RESOLUTION_INDEX,
        Kernel.T7_AIN_ALL_RESOLUTION_INDEX
    ]
    if type(addr_list) == type([]):
        if 0 != len(addr_list):
            for addr in addr_list:
                try:
                    test = res_addr.index(addr)
                except ValueError:
                    if display:
                        print("Address: " + str(addr) + " is an invalid resolution address.")
                    return -1
            return 1
        else:
            return -2
    elif isinstance(addr_list, int):
        try:
            test = res_addr.index(addr_list)
        except ValueError:
            if display:
                print("Address: " + str(addr_list) + " is an invalid input resolution address.")
            return -1
        return 2
    else:
        if display:
            print("Found " + str(type(addr_list)) + " instead of " + str(type([])) + " or " + str(int))
        return -3


def settling_addr_validator(addr_list, display=0):
    settling_addr = [
        Kernel.T7_AIN0_SETTLING_US, Kernel.T7_AIN1_SETTLING_US, Kernel.T7_AIN2_SETTLING_US,
        Kernel.T7_AIN3_SETTLING_US, Kernel.T7_AIN4_SETTLING_US, Kernel.T7_AIN5_SETTLING_US,
        Kernel.T7_AIN6_SETTLING_US, Kernel.T7_AIN7_SETTLING_US, Kernel.T7_AIN8_SETTLING_US,
        Kernel.T7_AIN9_SETTLING_US, Kernel.T7_AIN10_SETTLING_US, Kernel.T7_AIN11_SETTLING_US,
        Kernel.T7_AIN12_SETTLING_US, Kernel.T7_AIN13_SETTLING_US, Kernel.T7_AIN14_SETTLING_US,
        Kernel.T7_AIN15_SETTLING_US, Kernel.T7_AIN16_SETTLING_US, Kernel.T7_AIN17_SETTLING_US,
        Kernel.T7_AIN18_SETTLING_US, Kernel.T7_AIN19_SETTLING_US, Kernel.T7_AIN20_SETTLING_US,
        Kernel.T7_AIN21_SETTLING_US, Kernel.T7_AIN22_SETTLING_US, Kernel.T7_AIN23_SETTLING_US,
        Kernel.T7_AIN24_SETTLING_US, Kernel.T7_AIN25_SETTLING_US, Kernel.T7_AIN26_SETTLING_US,
        Kernel.T7_AIN27_SETTLING_US, Kernel.T7_AIN28_SETTLING_US, Kernel.T7_AIN29_SETTLING_US,
        Kernel.T7_AIN30_SETTLING_US, Kernel.T7_AIN31_SETTLING_US, Kernel.T7_AIN32_SETTLING_US,
        Kernel.T7_AIN33_SETTLING_US, Kernel.T7_AIN34_SETTLING_US, Kernel.T7_AIN35_SETTLING_US,
        Kernel.T7_AIN36_SETTLING_US, Kernel.T7_AIN37_SETTLING_US, Kernel.T7_AIN38_SETTLING_US,
        Kernel.T7_AIN39_SETTLING_US, Kernel.T7_AIN40_SETTLING_US, Kernel.T7_AIN41_SETTLING_US,
        Kernel.T7_AIN42_SETTLING_US, Kernel.T7_AIN43_SETTLING_US, Kernel.T7_AIN44_SETTLING_US,
        Kernel.T7_AIN45_SETTLING_US, Kernel.T7_AIN46_SETTLING_US, Kernel.T7_AIN47_SETTLING_US,
        Kernel.T7_AIN48_SETTLING_US, Kernel.T7_AIN49_SETTLING_US, Kernel.T7_AIN50_SETTLING_US,
        Kernel.T7_AIN51_SETTLING_US, Kernel.T7_AIN52_SETTLING_US, Kernel.T7_AIN53_SETTLING_US,
        Kernel.T7_AIN54_SETTLING_US, Kernel.T7_AIN55_SETTLING_US, Kernel.T7_AIN56_SETTLING_US,
        Kernel.T7_AIN57_SETTLING_US, Kernel.T7_AIN58_SETTLING_US, Kernel.T7_AIN59_SETTLING_US,
        Kernel.T7_AIN60_SETTLING_US, Kernel.T7_AIN61_SETTLING_US, Kernel.T7_AIN62_SETTLING_US,
        Kernel.T7_AIN63_SETTLING_US, Kernel.T7_AIN64_SETTLING_US, Kernel.T7_AIN65_SETTLING_US,
        Kernel.T7_AIN66_SETTLING_US, Kernel.T7_AIN67_SETTLING_US, Kernel.T7_AIN68_SETTLING_US,
        Kernel.T7_AIN69_SETTLING_US, Kernel.T7_AIN70_SETTLING_US, Kernel.T7_AIN71_SETTLING_US,
        Kernel.T7_AIN72_SETTLING_US, Kernel.T7_AIN73_SETTLING_US, Kernel.T7_AIN74_SETTLING_US,
        Kernel.T7_AIN75_SETTLING_US, Kernel.T7_AIN76_SETTLING_US, Kernel.T7_AIN77_SETTLING_US,
        Kernel.T7_AIN78_SETTLING_US, Kernel.T7_AIN79_SETTLING_US, Kernel.T7_AIN80_SETTLING_US,
        Kernel.T7_AIN81_SETTLING_US, Kernel.T7_AIN82_SETTLING_US, Kernel.T7_AIN83_SETTLING_US,
        Kernel.T7_AIN84_SETTLING_US, Kernel.T7_AIN85_SETTLING_US, Kernel.T7_AIN86_SETTLING_US,
        Kernel.T7_AIN87_SETTLING_US, Kernel.T7_AIN88_SETTLING_US, Kernel.T7_AIN89_SETTLING_US,
        Kernel.T7_AIN90_SETTLING_US, Kernel.T7_AIN91_SETTLING_US, Kernel.T7_AIN92_SETTLING_US,
        Kernel.T7_AIN93_SETTLING_US, Kernel.T7_AIN94_SETTLING_US, Kernel.T7_AIN95_SETTLING_US,
        Kernel.T7_AIN96_SETTLING_US, Kernel.T7_AIN97_SETTLING_US, Kernel.T7_AIN98_SETTLING_US,
        Kernel.T7_AIN99_SETTLING_US, Kernel.T7_AIN100_SETTLING_US, Kernel.T7_AIN101_SETTLING_US,
        Kernel.T7_AIN102_SETTLING_US, Kernel.T7_AIN103_SETTLING_US, Kernel.T7_AIN104_SETTLING_US,
        Kernel.T7_AIN105_SETTLING_US, Kernel.T7_AIN106_SETTLING_US, Kernel.T7_AIN107_SETTLING_US,
        Kernel.T7_AIN108_SETTLING_US, Kernel.T7_AIN109_SETTLING_US, Kernel.T7_AIN110_SETTLING_US,
        Kernel.T7_AIN111_SETTLING_US, Kernel.T7_AIN112_SETTLING_US, Kernel.T7_AIN113_SETTLING_US,
        Kernel.T7_AIN114_SETTLING_US, Kernel.T7_AIN115_SETTLING_US, Kernel.T7_AIN116_SETTLING_US,
        Kernel.T7_AIN117_SETTLING_US, Kernel.T7_AIN118_SETTLING_US, Kernel.T7_AIN119_SETTLING_US,
        Kernel.T7_AIN120_SETTLING_US, Kernel.T7_AIN121_SETTLING_US, Kernel.T7_AIN122_SETTLING_US,
        Kernel.T7_AIN123_SETTLING_US, Kernel.T7_AIN124_SETTLING_US, Kernel.T7_AIN125_SETTLING_US,
        Kernel.T7_AIN126_SETTLING_US, Kernel.T7_AIN127_SETTLING_US, Kernel.T7_AIN128_SETTLING_US,
        Kernel.T7_AIN129_SETTLING_US, Kernel.T7_AIN130_SETTLING_US, Kernel.T7_AIN131_SETTLING_US,
        Kernel.T7_AIN132_SETTLING_US, Kernel.T7_AIN133_SETTLING_US, Kernel.T7_AIN134_SETTLING_US,
        Kernel.T7_AIN135_SETTLING_US, Kernel.T7_AIN136_SETTLING_US, Kernel.T7_AIN137_SETTLING_US,
        Kernel.T7_AIN138_SETTLING_US, Kernel.T7_AIN139_SETTLING_US, Kernel.T7_AIN140_SETTLING_US,
        Kernel.T7_AIN141_SETTLING_US, Kernel.T7_AIN142_SETTLING_US, Kernel.T7_AIN143_SETTLING_US,
        Kernel.T7_AIN144_SETTLING_US, Kernel.T7_AIN145_SETTLING_US, Kernel.T7_AIN146_SETTLING_US,
        Kernel.T7_AIN147_SETTLING_US, Kernel.T7_AIN148_SETTLING_US, Kernel.T7_AIN149_SETTLING_US,
        Kernel.T7_AIN150_SETTLING_US, Kernel.T7_AIN151_SETTLING_US, Kernel.T7_AIN152_SETTLING_US,
        Kernel.T7_AIN153_SETTLING_US, Kernel.T7_AIN154_SETTLING_US, Kernel.T7_AIN155_SETTLING_US,
        Kernel.T7_AIN156_SETTLING_US, Kernel.T7_AIN157_SETTLING_US, Kernel.T7_AIN158_SETTLING_US,
        Kernel.T7_AIN159_SETTLING_US, Kernel.T7_AIN160_SETTLING_US, Kernel.T7_AIN161_SETTLING_US,
        Kernel.T7_AIN162_SETTLING_US, Kernel.T7_AIN163_SETTLING_US, Kernel.T7_AIN164_SETTLING_US,
        Kernel.T7_AIN165_SETTLING_US, Kernel.T7_AIN166_SETTLING_US, Kernel.T7_AIN167_SETTLING_US,
        Kernel.T7_AIN168_SETTLING_US, Kernel.T7_AIN169_SETTLING_US, Kernel.T7_AIN170_SETTLING_US,
        Kernel.T7_AIN171_SETTLING_US, Kernel.T7_AIN172_SETTLING_US, Kernel.T7_AIN173_SETTLING_US,
        Kernel.T7_AIN174_SETTLING_US, Kernel.T7_AIN175_SETTLING_US, Kernel.T7_AIN176_SETTLING_US,
        Kernel.T7_AIN177_SETTLING_US, Kernel.T7_AIN178_SETTLING_US, Kernel.T7_AIN179_SETTLING_US,
        Kernel.T7_AIN180_SETTLING_US, Kernel.T7_AIN181_SETTLING_US, Kernel.T7_AIN182_SETTLING_US,
        Kernel.T7_AIN183_SETTLING_US, Kernel.T7_AIN184_SETTLING_US, Kernel.T7_AIN185_SETTLING_US,
        Kernel.T7_AIN186_SETTLING_US, Kernel.T7_AIN187_SETTLING_US, Kernel.T7_AIN188_SETTLING_US,
        Kernel.T7_AIN189_SETTLING_US, Kernel.T7_AIN190_SETTLING_US, Kernel.T7_AIN191_SETTLING_US,
        Kernel.T7_AIN192_SETTLING_US, Kernel.T7_AIN193_SETTLING_US, Kernel.T7_AIN194_SETTLING_US,
        Kernel.T7_AIN195_SETTLING_US, Kernel.T7_AIN196_SETTLING_US, Kernel.T7_AIN197_SETTLING_US,
        Kernel.T7_AIN198_SETTLING_US, Kernel.T7_AIN199_SETTLING_US, Kernel.T7_AIN200_SETTLING_US,
        Kernel.T7_AIN201_SETTLING_US, Kernel.T7_AIN202_SETTLING_US, Kernel.T7_AIN203_SETTLING_US,
        Kernel.T7_AIN204_SETTLING_US, Kernel.T7_AIN205_SETTLING_US, Kernel.T7_AIN206_SETTLING_US,
        Kernel.T7_AIN207_SETTLING_US, Kernel.T7_AIN208_SETTLING_US, Kernel.T7_AIN209_SETTLING_US,
        Kernel.T7_AIN210_SETTLING_US, Kernel.T7_AIN211_SETTLING_US, Kernel.T7_AIN212_SETTLING_US,
        Kernel.T7_AIN213_SETTLING_US, Kernel.T7_AIN214_SETTLING_US, Kernel.T7_AIN215_SETTLING_US,
        Kernel.T7_AIN216_SETTLING_US, Kernel.T7_AIN217_SETTLING_US, Kernel.T7_AIN218_SETTLING_US,
        Kernel.T7_AIN219_SETTLING_US, Kernel.T7_AIN220_SETTLING_US, Kernel.T7_AIN221_SETTLING_US,
        Kernel.T7_AIN222_SETTLING_US, Kernel.T7_AIN223_SETTLING_US, Kernel.T7_AIN224_SETTLING_US,
        Kernel.T7_AIN225_SETTLING_US, Kernel.T7_AIN226_SETTLING_US, Kernel.T7_AIN227_SETTLING_US,
        Kernel.T7_AIN228_SETTLING_US, Kernel.T7_AIN229_SETTLING_US, Kernel.T7_AIN230_SETTLING_US,
        Kernel.T7_AIN231_SETTLING_US, Kernel.T7_AIN232_SETTLING_US, Kernel.T7_AIN233_SETTLING_US,
        Kernel.T7_AIN234_SETTLING_US, Kernel.T7_AIN235_SETTLING_US, Kernel.T7_AIN236_SETTLING_US,
        Kernel.T7_AIN237_SETTLING_US, Kernel.T7_AIN238_SETTLING_US, Kernel.T7_AIN239_SETTLING_US,
        Kernel.T7_AIN240_SETTLING_US, Kernel.T7_AIN241_SETTLING_US, Kernel.T7_AIN242_SETTLING_US,
        Kernel.T7_AIN243_SETTLING_US, Kernel.T7_AIN244_SETTLING_US, Kernel.T7_AIN245_SETTLING_US,
        Kernel.T7_AIN246_SETTLING_US, Kernel.T7_AIN247_SETTLING_US, Kernel.T7_AIN248_SETTLING_US,
        Kernel.T7_AIN249_SETTLING_US, Kernel.T7_AIN250_SETTLING_US, Kernel.T7_AIN251_SETTLING_US,
        Kernel.T7_AIN252_SETTLING_US, Kernel.T7_AIN253_SETTLING_US, Kernel.T7_AIN254_SETTLING_US,
        Kernel.T7_AIN_ALL_SETTLING_US
    ]
    if type(addr_list) == type([]):
        if 0 != len(addr_list):
            for addr in addr_list:
                try:
                    test = settling_addr.index(addr)
                except ValueError:
                    if display:
                        print("Address: " + str(addr) + " is an invalid settling address.")
                    return -1
            return 1
        else:
            return -2
    elif isinstance(addr_list, int):
        try:
            test = settling_addr.index(addr_list)
        except ValueError:
            if display:
                print("Address: " + str(addr_list) + " is an invalid settling address.")
            return -1
        return 2
    else:
        if display:
            print("Found " + str(type(addr_list)) + " instead of " + str(type([])) + " or " + str(int))
        return -3


def range_validator(ranges, display=0):
    range_list = [
        10, 1, 10.0, 1.0, 0.1, 0.01
    ]
    if type(ranges) == type([]):
        if 0 != len(ranges):
            for range_v in ranges:
                try:
                    test = range_list.index(range_v)
                except ValueError:
                    if display:
                        print("Value " + str(range_v) + " is not permitted.")
                        print("Value permitted is:")
                        for value in range_list:
                            print(value)
                    return -1
            return 1
        else:
            return -2
    elif isinstance(ranges, int):
        try:
            test = range_list.index(ranges)
        except ValueError:
            if display:
                print("Value " + str(ranges) + " is not permitted.")
                print("Value permitted is:")
                for value in range_list:
                    print(value)
            return -1
        return 2
    elif isinstance(ranges, float):
        try:
            test = range_list.index(ranges)
        except ValueError:
            if display:
                print("Value " + str(ranges) + " is not permitted.")
                print("Value permitted is:")
                for value in range_list:
                    print(value)
            return -1
        return 3
    else:
        if display:
            print(
                "Found " + str(type(ranges)) + " instead of " + str(type([])) + " or " + str(int) + " or " + str(float)
            )
        return -3


def dac_addr_validator(addr_list, display=0):
    dac_addr = [
        Kernel.T7_DAC0, Kernel.T7_DAC1
    ]
    if type(addr_list) == type([]):
        if 0 != len(addr_list):
            for addr in addr_list:
                try:
                    test = dac_addr.index(addr)
                except ValueError:
                    if display:
                        print("Address: " + str(addr) + " is an invalid output analog address.")
                    return -1
            return 1
        else:
            return -2
    elif isinstance(addr_list, int):
        try:
            test = dac_addr.index(addr_list)
        except ValueError:
            if display:
                print("Address: " + str(addr_list) + " is an invalid output analog address.")
            return -1
        return 2
    else:
        if display:
            print("Found " + str(type(addr_list)) + " instead of " + str(type([])) + " or " + str(int))
        return -3


def dac_output_voltage_validator(values_list, display=0):
    if type(values_list) == type([]):
        if 0 != len(values_list):
            for value in values_list:
                if (not isinstance(values_list, int)) and (not isinstance(values_list, float)):
                    return -3
                elif not (-10.0 <= values_list <= 10.0):
                    return -1
            return 1
        else:
            return -2
    elif isinstance(values_list, int):
        if -10 <= values_list <= 10:
            return 0
        else:
            return -1
    elif isinstance(values_list, float):
        if -10.0 <= values_list <= 10.0:
            return 0
        else:
            return -1
    else:
        if display:
            print(
                "Found " + str(type(values_list)) +
                " instead of " + str(type([])) + " or " + str(int) + " or " + str(float)
            )
        return -3


def settling_time_validator(settling_list, display=0):
    settling_allowed = [
        10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000
    ]
    if type(settling_list) == type([]):
        if 0 != len(settling_list):
            for res_v in settling_list:
                try:
                    test = settling_allowed.index(res_v)
                except ValueError:
                    if display:
                        print("Value " + str(settling_list) + " is not permitted.")
                        print("Value permitted is:")
                        for value in settling_allowed:
                            print(value)
                    return -1
            return 1
        else:
            return -2
    elif isinstance(settling_list, int):
        try:
            test = settling_allowed.index(settling_list)
        except ValueError:
            if display:
                print("Value " + str(settling_list) + " is not permitted.")
                print("Value permitted is:")
                for value in settling_allowed:
                    print(value)
            return -1
        return 0
    else:
        if display:
            print(
                "Found " + str(type(settling_list)) +
                " instead of " + str(type([])) + " or " + str(int)
            )
        return -3


def res_validator(res_list, display=0):
    resolution_list = [
        "auto", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    ]
    if type(res_list) == type([]):
        if 0 != len(res_list):
            for res_v in res_list:
                try:
                    test = resolution_list.index(res_v)
                except ValueError:
                    if display:
                        print("Value " + str(res_list) + " is not permitted.")
                        print("Value permitted is:")
                        for value in resolution_list:
                            print(value)
                    return -1
            return 1
        else:
            return -2
    elif isinstance(res_list, int):
        try:
            test = resolution_list.index(res_list)
        except ValueError:
            if display:
                print("Value " + str(res_list) + " is not permitted.")
                print("Value permitted is:")
                for value in resolution_list:
                    print(value)
            return -1
        return 0
    else:
        if display:
            print(
                "Found " + str(type(res_list)) +
                " instead of " + str(type([])) + " or " + str(int)
            )
        return -3


"""
/**********************************************************************************************************************/
/***************************************************ERROR FUNCTION*****************************************************/
/**********************************************************************************************************************/
"""


def dac_addr_error(error_code, addr_list):
    if -3 == error_code:
        print("Invalid address type.")
        dac_addr_validator(addr_list, 1)
    elif -1 == error_code:
        print("Invalid address for analog output.")
        ain_addr_validator(addr_list, 1)
    elif -2 == error_code:
        print("Address list is empty.")


def range_error(error_code, range_list):
    if -3 == error_code:
        print("Invalid address type.")
        range_validator(range_list, 1)
    elif -1 == error_code:
        print("Invalid address for analog input.")
        range_validator(range_list, 1)
    elif -2 == error_code:
        print("Address list is empty.")


def ain_addr_error(error_code, addr_list):
    if -3 == error_code:
        print("Invalid address type.")
        ain_addr_validator(addr_list, 1)
    elif -1 == error_code:
        print("Invalid address for analog input.")
        ain_addr_validator(addr_list, 1)
    elif -2 == error_code:
        print("Address list is empty.")


def settling_addr_error(error_code, addr_list):
    if -3 == error_code:
        print("Invalid address type.")
        ain_addr_validator(addr_list, 1)
    elif -1 == error_code:
        print("Invalid settling address.")
        ain_addr_validator(addr_list, 1)
    elif -2 == error_code:
        print("Address list is empty.")


def res_addr_error(error_code, addr_list):
    if -3 == error_code:
        print("Invalid address type.")
        ain_addr_validator(addr_list, 1)
    elif -1 == error_code:
        print("Invalid resolution address.")
        ain_addr_validator(addr_list, 1)
    elif -2 == error_code:
        print("Address list is empty.")


def voltage_error(error_code, voltage_list):
    if -3 == error_code:
        print("Invalid voltage type.")
        dac_output_voltage_validator(voltage_list, 1)
    elif -1 == error_code:
        print("Invalid voltage value it must be between -10v and 10v.")
        dac_output_voltage_validator(voltage_list, 1)
    elif -2 == error_code:
        print("Voltage list is empty.")


def settling_error(error_code, settling_list):
    if -3 == error_code:
        print("Invalid settling type.")
        settling_list(settling_list, 1)
    elif -1 == error_code:
        print("Invalid settling value.")
        settling_time_validator(settling_list, 1)
    elif -2 == error_code:
        print("settling time list is empty.")


def res_error(error_code, res_list):
    if -3 == error_code:
        print("Invalid resolution type.")
        res_validator(res_list, 1)
    elif -1 == error_code:
        print("Invalid resolution value.")
        res_validator(res_list, 1)
    elif -2 == error_code:
        print("resolution list is empty.")
