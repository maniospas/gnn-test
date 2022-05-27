import gnntf
from experiments.experiment_setup import dgl_setup


gnntf.set_seed(0)
G, labels, features, train, valid, test = dgl_setup("cora")
num_classes = len(set(labels))
gnn = gnntf.APPNP(gnntf.graph2adj(G), features, num_classes=num_classes)
gnn.add(gnntf.PPRSweep())

gnn.train(train=gnntf.NodeClassification(train, labels[train]),
          valid=gnntf.NodeClassification(valid, labels[valid]))

prediction = gnn.predict(gnntf.NodeClassification(test))
accuracy = gnntf.acc(prediction, labels[test])
print(accuracy)
