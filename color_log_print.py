#color text
cClear = '\033[0m'
cBlack = '\033[30m'
cRed = '\033[31m'
cGreen = '\033[32m'
cYellow = '\033[33m'
cBlue = '\033[34m'
cMagenta = '\033[35m'
cCyan = '\033[36m'
cWhite = '\033[37m'
cBright_Black = '\033[30;1m'    #or '\033[1;30m
cBright_Red = '\033[31;1m'      #or '\033[1;31m
cBright_Green = '\033[32;1m'    #or '\033[1;32m
cBright_Yellow = '\033[33;1m'   #or '\033[1;33m
cBright_Blue = '\033[34;1m'     #or '\033[1;34m
cBright_Magenta = '\033[35;1m'  #or '\033[1;35m
cBright_Cyan = '\033[36;1m'     #or '\033[1;36m
cBright_White = '\033[37;1m'    #or '\033[1;37m
cLight_Gray = '\033[90m'
cDark_Red = '\033[91m'
cDark_Green = '\033[92m'
cDark_Yellow = '\033[93m'



import colorama

# Initialize colorama
colorama.init()
#color text
colorama_c_Black    = colorama.Fore.BLACK
colorama_c_White    = colorama.Fore.WHITE
colorama_c_Magenta  = colorama.Fore.MAGENTA
colorama_c_Cyan     = colorama.Fore.CYAN
colorama_c_Red      = colorama.Fore.RED
colorama_c_Green    = colorama.Fore.GREEN
colorama_c_Blue     = colorama.Fore.BLUE
colorama_c_Yellow   = colorama.Fore.YELLOW

#color background
colorama_b_Black    = colorama.Back.BLACK
colorama_b_White    = colorama.Back.WHITE
colorama_b_Magenta  = colorama.Back.MAGENTA
colorama_b_Cyan     = colorama.Back.CYAN
colorama_b_Red      = colorama.Back.RED
colorama_b_Green    = colorama.Back.GREEN
colorama_b_Blue     = colorama.Back.BLUE
colorama_b_Yellow   = colorama.Back.YELLOW

#high ligh entire the line
colorama_line_bright = colorama.Style.BRIGHT 
#for reset
colorama_color_reset = colorama.Style.RESET_ALL

#for testing
# print(f"{colorama_b_Cyan}[13-03-2023]{colorama_color_reset} [10:55:05] {cBlack}=====>{cClear}")
# print(f"{colorama_b_Magenta}Hello w{colorama_color_reset}or{colorama_b_Cyan}ld!{colorama_color_reset}")
