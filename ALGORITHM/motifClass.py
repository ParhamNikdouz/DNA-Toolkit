from ALGORITHM.fileClass import File  # Import File Class
from ALGORITHM.sequenceClass import Sequence  # Import Fasta Class
from ALGORITHM.excelClass import Excel  # Import Fasta Class
from Bio.Seq import Seq  # Import Sequence BioPython
from Bio.Alphabet import generic_dna
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
import sklearn.cluster
from mpl_toolkits.mplot3d import Axes3D
from itertools import cycle, islice
import skfuzzy as fuzz
from matplotlib.colors import LogNorm
from sklearn import mixture

class Motif():
    motifs = []
    numNmersMotifsDic = {}
    data_set = []  # Define variable for clustering
    f1 = 0;
    f2 = 1;
    f3 = 2;
    c1 = "";
    c2 = "";
    c3 = "";
    my_dna = []
    colors = np.array([]);  # except affinity

    # Initial method
    def __init__(self, fasta_addr, exel_addr):
        seq = Sequence()  # Create object from sequence
        self.sequences = seq.sequence(fasta_addr)

        valueObj = Excel()  # Create object from excel class
        valueObj.openExcel(exel_addr);
        self.motifs = valueObj.values

        self.f1 = 0;
        self.f2 = 1;
        self.f3 = 2;

        self.c1 = "";
        self.c2 = "";
        self.c3 = "";

        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            self.my_dna.append(Seq(dna, generic_dna));

        self.colors = np.array(list(islice(cycle(
            ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf', '#a65628', '#984ea3', '#999999', '#e41a1c', '#dede00',
             '#000000']), 10)));

    def setPlotFields(self, sf1, sf2, sf3):
        # s = [f11,f22,f33];
        # s.sort();
        # self.f1 = s[0]-1;
        # self.f2 =s[1]-1;
        # self.f3 = s[2]-1;
        self.c1 = sf1;
        self.c2 = sf2;
        self.c3 = sf3;

    # Print motifs
    def printMotif(self):
        print(self.motifs)

        # Save motifs in list

    ##    def motifList(self,exelAddr):
    ##        valueObj = Excel() #Create object from excel class
    ##        valueObj.openExcel(exelAddr);
    ##        self.motifs = valueObj.values

    def getLenMotif(self):
        print(len(self.motifs))

    # Calculate count of motifs in sequence with overlap
    def countMotif(self):

        pattern = ''
        countMotifs = {}

        # Print length of motifs
        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)

            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                # Number of repeat pattern
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

    # Calculate number of n-mers motifs in sequence
    def numNmersMotifs(self):

        pattern = ''
        countMotifs = {}

        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)

            summ = [0] * 5;  # Define summ variable

            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))

            for value in countMotifs.keys():
                if (len(value) == 1):
                    temp = countMotifs[value]  # This is a list
                    summ[0] += temp[0]
                elif (len(value) == 2):
                    temp = countMotifs[value]
                    summ[1] += temp[0]
                elif (len(value) == 3):
                    temp = countMotifs[value]
                    summ[2] += temp[0]
                elif (len(value) == 4):
                    temp = countMotifs[value]
                    summ[3] += temp[0]
                elif (len(value) == 5):
                    temp = countMotifs[value]
                    summ[4] += temp[0]
            self.numNmersMotifsDic[i] = []
            self.numNmersMotifsDic[i].append(summ[0])
            self.numNmersMotifsDic[i].append(summ[1])
            self.numNmersMotifsDic[i].append(summ[2])
            self.numNmersMotifsDic[i].append(summ[3])
            self.numNmersMotifsDic[i].append(summ[4])

    # Calculate Frequency of motifs in sequence
    def frequencyMotifs(self):
        pattern = ''
        countMotifs = {}

        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)
            print('Sequence', i + 1)

            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                countMotifs[pattern] = []
                countMotifs[pattern].append(my_dna.count_overlap(pattern))
            # data_set.append(countMotifs)

            for key, value in countMotifs.items():
                if (len(key) == 1):
                    temp = value[0]  # This is a list
                    percentage = '%.2f' % (
                    (temp / self.numNmersMotifsDic[i][0]) * 100)  # Caculate Percentage and show 2 decimal
                    print('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 2):
                    temp = value[0]
                    percentage = '%.2f' % ((temp / self.numNmersMotifsDic[i][1]) * 100)
                    print('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 3):
                    temp = value[0]
                    percentage = '%.2f' % ((temp / self.numNmersMotifsDic[i][2]) * 100)
                    print('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 4):
                    temp = value[0]
                    percentage = '%.2f' % ((temp / self.numNmersMotifsDic[i][3]) * 100)
                    print('Frequency of', key, '==>', percentage, '%')
                elif (len(key) == 5):
                    temp = value[0]
                    percentage = '%.2f' % ((temp / self.numNmersMotifsDic[i][4]) * 100)
                    print('Frequency of', key, '==>', percentage, '%')

    def fill_dataSet(self, listOfMotifs):
        self.data_set.clear();

        list_set = set(listOfMotifs);
        lom = list(list_set);
        pattern = ''
        countMotifs = {}
        # self.motifList();
        for i in range(len(self.my_dna)):
            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                if (pattern in lom):
                    countMotifs[pattern] = self.my_dna[i].count_overlap(pattern)
            self.data_set.append(countMotifs.copy())
        if (self.c1 != ""):
            lk = list(self.data_set[0].keys())
            for i in range(0, len(lk)):
                if (self.c1 == lk[i]):
                    self.f1 = i;
                if (self.c2 == lk[i]):
                    self.f2 = i;
                if (self.c3 == lk[i]):
                    self.f3 = i;
            ss = [self.f1, self.f2, self.f3];
            ss.sort();
            self.f1 = ss[0];
            self.f2 = ss[1];
            self.f3 = ss[2];

    def plt_2d(self, A, Labels, title):
        # colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
        #                                      '#f781bf', '#a65628', '#984ea3',
        #                                      '#999999', '#e41a1c', '#dede00', '#000000']), 10)));
        for i in range(len(A)):
            if (i < len(A)):
                plt.plot(A[i][self.f1], A[i][self.f2], '.', color=self.colors[Labels[i]])

        plt.title(title);
        fig = plt.gcf()
        fig.canvas.set_window_title("clustring by " + title + " algorithm(2D)");
        plt.ylabel('y', fontsize=20);
        plt.xlabel('x', fontsize=20);

    def plt_3d(self, A, Labels, l, title):
        # colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
        #                                      '#f781bf', '#a65628', '#984ea3',
        #                                      '#999999', '#e41a1c', '#dede00', '#000000']), 10)));

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_title(title);
        ax.set_ylabel("y");
        ax.set_xlabel("x");
        ax.set_zlabel("z");
        fig = plt.gcf()
        fig.canvas.set_window_title("clustring by " + title + " algorithm(3D)");
        for i in range(0, len(l)):
            ax.scatter(A[i][self.f1], A[i][self.f2], A[i][self.f3], '.', color=self.colors[Labels[i]], s=5)
        return ax;

    def clustring_kmeans(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        kmeans = sklearn.cluster.KMeans(n_clusters=n)
        kmeans.fit(A)
        Centroids = kmeans.cluster_centers_
        Labels = kmeans.labels_

        if (dem == 2):
            self.plt_2d(A, Labels, "KMeans");
            plt.scatter(Centroids[:, self.f1], Centroids[:, self.f2], marker="x", s=100)
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, Labels, l, "KMeans").scatter(Centroids[:, self.f1], Centroids[:, self.f2],
                                                        Centroids[:, self.f3], marker="x", s=100, c="black");
            plt.show()
        else:
            print("dem bad value");

    def clustring_MiniBatchKMeans(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        mbk = sklearn.cluster.MiniBatchKMeans(n_clusters=n)
        mbk.fit(A);
        Centroids = mbk.cluster_centers_
        Labels = mbk.labels_
        if (dem == 2):
            self.plt_2d(A, Labels, "MiniBatchKMeans");
            plt.scatter(Centroids[:, self.f1], Centroids[:, self.f2], marker="x", s=100)
            plt.show()

        elif (dem == 3):
            self.plt_3d(A, Labels, l, "MiniBatchKMeans").scatter(Centroids[:, self.f1], Centroids[:, self.f2],
                                                                 Centroids[:, self.f3], marker="x", s=100, c="black");
            plt.show()
        else:
            print("dem bad value");

    def clustring_AgglomerativeClustering(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        agg = sklearn.cluster.AgglomerativeClustering(n_clusters=n)
        agg.fit(A);
        Labels = agg.labels_

        if (dem == 2):
            figg = plt.figure();
            self.plt_2d(A, Labels, "Agglomerative");
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, Labels, l, "Agglomerative");
            plt.show()
        else:
            print("dem bad value");

    def clustring_SpectralClustering(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        agg = sklearn.cluster.SpectralClustering(n_clusters=n, eigen_solver='arpack', affinity="nearest_neighbors")
        agg.fit(A);
        Labels = agg.labels_

        if (dem == 2):
            figg = plt.figure();
            self.plt_2d(A, Labels, "Spectral");
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, Labels, l, "Spectral");
            plt.show()
        else:
            print("dem bad value");

    def clustring_Birch(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        agg = sklearn.cluster.Birch(n_clusters=n)
        agg.fit(A);
        Labels = agg.labels_

        if (dem == 2):
            self.plt_2d(A, Labels, "Birch");
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, Labels, l, "Birch")
            plt.show()
        else:
            print("dem bad value");

    def clustring_cmeans(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));
        A = np.array(l);

        # colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']
        ss = set(listOfMotifs);
        lo = list(ss);
        if (len(lo) == 2):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel()))
        elif (len(lo) == 3):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel()))
        elif (len(lo) == 4):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel()))
        elif (len(lo) == 5):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel(),
                                 (A[:, 4:5]).ravel()))
        elif (len(lo) == 6):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel(),
                                 (A[:, 4:5]).ravel(), (A[:, 5:6]).ravel()))
        elif (len(lo) == 7):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel(),
                                 (A[:, 4:5]).ravel(), (A[:, 5:6]).ravel(), (A[:, 6:7]).ravel()))
        elif (len(lo) == 8):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel(),
                                 (A[:, 4:5]).ravel(), (A[:, 5:6]).ravel(), (A[:, 6:7]).ravel(), (A[:, 7:8]).ravel()))
        elif (len(lo) == 9):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel(),
                                 (A[:, 4:5]).ravel(), (A[:, 5:6]).ravel(), (A[:, 6:7]).ravel(), (A[:, 7:8]).ravel(),
                                 (A[:, 8:9]).ravel()))
        elif (len(lo) == 10):
            alldata = np.vstack(((A[:, 0:1]).ravel(), (A[:, 1:2]).ravel(), (A[:, 2:3]).ravel(), (A[:, 3:4]).ravel(),
                                 (A[:, 4:5]).ravel(), (A[:, 5:6]).ravel(), (A[:, 6:7]).ravel(), (A[:, 7:8]).ravel(),
                                 (A[:, 8:9]).ravel(), (A[:, 9:10]).ravel()))
        else:
            print("dem bad value");
        fpcs = []

        xpts = np.array([]);
        ypts = np.array([]);
        zpts = np.array([]);
        for i in range(0, len(l)):
            ll = []
            ll.append(l[i][self.f1]);
            xpts = np.append(xpts, ll.copy());
            ll = []
            ll.append(l[i][self.f2]);
            ypts = np.append(ypts, ll.copy());
            if (len(listOfMotifs) > 2):
                ll = []
                ll.append(l[i][self.f3]);
                zpts = np.append(zpts, ll.copy());

        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(alldata, n, 4, error=0.005, maxiter=1000, init=None)
        fpcs.append(fpc)
        cluster_membership = np.argmax(u, axis=0)

        if (dem == 2):
            for j in range(n):
                plt.plot(xpts[cluster_membership == j], ypts[cluster_membership == j], '.', color=self.colors[j],
                         markersize=5)
            plt.scatter(cntr[:, self.f1], cntr[:, self.f2], marker="x", s=100)
            plt.title("Fuzzy-cmeans");
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by " + "Fuzzy-cmeans" + " algorithm(2D)");
            plt.ylabel('y', fontsize=20);
            plt.xlabel('x', fontsize=20);
        elif (dem == 3):
            fig = plt.figure()
            ax = Axes3D(fig)
            ax.set_title("Fuzzy-cmeans");
            ax.set_ylabel("y");
            ax.set_xlabel("x");
            ax.set_zlabel("z");
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by " + "Fuzzy-cmeans" + " algorithm(3D)");
            for j in range(n):
                ax.plot(xpts[cluster_membership == j], ypts[cluster_membership == j], zpts[cluster_membership == j],
                        '.', color=self.colors[j], markersize=5)
            ax.scatter(cntr[:, self.f1], cntr[:, self.f2], cntr[:, self.f3], marker="x", s=100)
        else:
            print("dem bad value");
        plt.show();

    def clustring_mixture_gaussian(self, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);
        t = A[:, self.f1:self.f1 + 2]
        clf = mixture.GaussianMixture(n_components=n, covariance_type='full')
        clf.fit(t);

        xmax = np.max(t[:, 0]);
        ymax = np.max(t[:, 1]);
        xmin = np.min(t[:, 0]);
        ymin = np.min(t[:, 1]);
        padd = 50;
        # display predicted scores by the model as a contour plot
        x = np.linspace(xmin - padd, xmax + padd)
        y = np.linspace(ymin - padd, ymax + padd)
        X, Y = np.meshgrid(x, y)
        XX = np.array([X.ravel(), Y.ravel()]).T
        Z = -clf.score_samples(XX)
        Z = Z.reshape(X.shape)

        CS = plt.contour(X, Y, Z, norm=LogNorm(vmin=1.0, vmax=1000.0),
                         levels=np.logspace(0, 3, 10))
        plt.scatter(t[:, 0], t[:, 1], 5)

        plt.title('GaussianMixture')
        plt.axis('tight')
        fig = plt.gcf()
        fig.canvas.set_window_title('GaussianMixture');
        plt.ylabel('y', fontsize=20);
        plt.xlabel('x', fontsize=20);
        plt.show()

    def clustring_AffinityPropagation(self, dem, listOfMotifs):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        af = sklearn.cluster.AffinityPropagation(preference=-50).fit(A);
        cluster_centers_indices = af.cluster_centers_indices_
        labels = af.labels_

        n_clusters_ = len(cluster_centers_indices)
        if (dem == 2):
            plt.title("AffinityPropagation\nEstimated number of clusters: " + str(n_clusters_));
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by AffinityPropagation algorithm(2D)");
            plt.ylabel('y', fontsize=20);
            plt.xlabel('x', fontsize=20);
            colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
            for k, col in zip(range(n_clusters_), colors):
                class_members = labels == k
                cluster_center = A[cluster_centers_indices[k]]
                plt.plot(A[class_members, self.f1], A[class_members, self.f2], col + '.')
                plt.plot(cluster_center[self.f1], cluster_center[self.f2], markerfacecolor=col,
                         markeredgecolor='k', markersize=14)
                for x in A[class_members]:
                    plt.plot([cluster_center[self.f1], x[self.f1]], [cluster_center[self.f2], x[self.f2]], col)
            plt.show()
        elif (dem == 3):
            fig = plt.figure()
            ax = Axes3D(fig)
            ax.set_title("AffinityPropagation\nEstimated number of clusters: " + str(n_clusters_));
            ax.set_ylabel("y");
            ax.set_xlabel("x");
            ax.set_zlabel("z");
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by " + "AffinityPropagation" + " algorithm(3D)");

            colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
            for k, col in zip(range(n_clusters_), colors):
                class_members = labels == k
                cluster_center = A[cluster_centers_indices[k]]
                ax.scatter(A[class_members, self.f1], A[class_members, self.f2], A[class_members, self.f3], '.',
                           color=col, s=7)
                for x in A[class_members]:
                    plt.plot([cluster_center[self.f1], x[self.f1]], [cluster_center[self.f2], x[self.f2]],
                             [cluster_center[self.f3], x[self.f3]], col)
            plt.show()
        else:
            print("dem bad value");

    def clustring_meanshift(self, dem, listOfMotifs):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);

        ms = sklearn.cluster.MeanShift();
        ms.fit(A)
        labels = ms.labels_
        cluster_centers = ms.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        # colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        if (dem == 2):
            plt.title("MeanShift\nEstimated number of clusters: " + str(n_clusters_));
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by MeanShift algorithm(2D)");
            plt.ylabel('y', fontsize=20);
            plt.xlabel('x', fontsize=20);

            for k, col in zip(range(n_clusters_), self.colors):
                my_members = labels == k
                cluster_center = cluster_centers[k]
                plt.plot(A[my_members, self.f1], A[my_members, self.f2], '.', color=col)
                plt.plot(cluster_center[self.f1], cluster_center[self.f2], 'o', markerfacecolor=col,
                         markeredgecolor='k', markersize=14)
        elif (dem == 3):
            fig = plt.figure()
            ax = Axes3D(fig)
            ax.set_title("MeanShift\nEstimated number of clusters: " + str(n_clusters_));
            ax.set_ylabel("y");
            ax.set_xlabel("x");
            ax.set_zlabel("z");
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by " + "MeanShift" + " algorithm(3D)");

            for k, col in zip(range(n_clusters_), self.colors):
                class_members = labels == k
                cluster_center = cluster_centers[k]
                ax.scatter(A[class_members, self.f1], A[class_members, self.f2], A[class_members, self.f3], '.',
                           color=col, s=7)
                ax.scatter(cluster_center[self.f1], cluster_center[self.f2], cluster_center[self.f3], 'o', color='k')
            plt.show()
        else:
            print("dem bad value");
        plt.show()
