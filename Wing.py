
from cc3d import CompuCellSetup
        

from WingSteppables import WingSteppable

CompuCellSetup.register_steppable(steppable=WingSteppable(frequency=1))


CompuCellSetup.run()
