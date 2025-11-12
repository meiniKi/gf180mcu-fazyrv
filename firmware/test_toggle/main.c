
#include "../soc.h"

void main(void)
{
  while(1)
  {
    GPO = 0xff;
    GPO = 0x00;
  }
}
