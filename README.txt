Changes made with respect to the original zsim are:
1. Added a configuration file "tcroadCA_OOO_core_2.cfg" which will enable the graph applications to run on zsim and it specifies the
   system parameters. This configuration file requires another configuration file which specifies the main memory parameters, and
   that is provided by "param.cfg" file. "tcroadCA_OOO_core_2.cfg" internally links "param.cfg" file.

2. Modified the MemAccessEventBase class. Added the core id(srcId) as a member variable.

3. Implemented the core-aware priority which will give priority to the memory requests from the core 0. The following represents the
   file name and line number on which changes are made to achieve core aware priority.
    detailed_mem.h : 343,346,347,352
    detailed_mem.cpp : 955,1138

