import Alg1
from Alg1 import *

Gael = Human('Gael','Ateneo de Manila University','BS MIS','Filipino')
Raine = Human('Raine','Ateneo de Manila University','BS MIS','Filipino')
Jack = Human('Jack','DLSU','BS CS','Filipino')

Gael.Connection(Raine,"Mutual Understanding Friends")
Gael.Connection(Jack,'Friend')
Jack.Connection(Raine,'Friend')

Gael.Relationships()

Gael.RelationshipChange(Raine,'Crush')

Gael.Relationships()

Gael.Mutual(Raine)
Raine.Mutual(Gael)
Jack.Mutual(Gael)