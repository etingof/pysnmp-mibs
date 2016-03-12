import os
from pysnmp.smi import builder, view, compiler, error

mibBuilder = builder.MibBuilder()

mib_dir = os.path.join(os.path.dirname(__file__), '..', 'pysnmp_mibs')

mibBuilder.addMibSources(builder.DirMibSource(mib_dir))
mibBuilder.loadModules()
mibView = view.MibViewController(mibBuilder)
