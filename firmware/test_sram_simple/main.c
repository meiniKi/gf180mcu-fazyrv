
#include "../types.h"
#include "../soc.h"

#define ADR_SRAM ((volatile uint32_t*)(0x10000000))
#define ADR_RAM  ((volatile uint32_t*)(0x20000000))

void main(void)
{
  *(ADR_SRAM+10UL) = 0xFF00FF00;
  
  if (*(ADR_SRAM+10UL) != 0xFF00FF00) { GPO = 4; goto done; };


  GPO = 5;

done:
  while (1);

}
