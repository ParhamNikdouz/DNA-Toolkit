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


############################################################################################
# Motif class                                                                               #
# In this class we add motif file to motif list                                             #
# You can print motifs, and get number of motifs in list                                    #
# We can get count repeated motifs with Overlap in each sequence by bioPython library       #
# Also we calculate sum of n-mers motifs in each sequnce for calculation frequency of motifs#
############################################################################################

class Motif():
    motifs = []
    numNmersMotifsDic = {}
    data_set = []  # Define variable for clustering

    # Initial method
    def __init__(self, fasta_addr, exel_addr):
        seq = Sequence()  # Create object from sequence
        self.sequences = seq.sequence(fasta_addr)

        valueObj = Excel()  # Create object from excel class
        valueObj.openExcel(exel_addr);
        self.motifs = valueObj.values

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
            print(countMotifs)

    # Calculate number of n-mers motifs in sequence
    def gui_CountMotif(self,i):

        import LIB.HTML as html

        # print (self.motifs)

        pattern = ''
        countMotifsList = []

        HTMLFILE = 'E:\MY CODES\PYTHON\DNA-Toolkit\htmlOutput\motifCount'+str(i)+'.html'
        f = open(HTMLFILE, 'w')

        t = html.Table(header_row=self.motifs)

        # Length of motifs
        #for i in range(3):
        dna = self.sequences[i]
        my_dna = Seq(dna, generic_dna)
        countMotifs = []
        for j in range(len(self.motifs)):
            pattern = self.motifs[j]
            # Number of repeat pattern
            countMotifs.append(my_dna.count_overlap(pattern))
        # countMotifsList.append(countMotifs)
        t.rows.append(countMotifs)

        htmlcode = str(t)
        print(htmlcode)
        f.write(htmlcode)
        f.write('<p>')
        print('-' * 79)


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
        pattern = ''
        countMotifs = {}
        # self.motifList();
        for i in range(len(self.sequences)):
            dna = self.sequences[i]
            my_dna = Seq(dna, generic_dna)

            for j in range(len(self.motifs)):
                pattern = self.motifs[j]
                if (pattern in listOfMotifs):
                    countMotifs[pattern] = my_dna.count_overlap(pattern)
            self.data_set.append(countMotifs.copy())

    def plt_2d(self, A, f1, f2, Labels, title):
        colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                             '#f781bf', '#a65628', '#984ea3',
                                             '#999999', '#e41a1c', '#dede00', '#000000']), 10)));
        for i in range(len(A)):
            if (i < len(A)):
                plt.plot(A[i][f1], A[i][f2], '.', color=colors[Labels[i]])

        plt.title(title);
        fig = plt.gcf()
        fig.canvas.set_window_title("clustring by " + title + " algorithm(2D)");
        plt.ylabel('y', fontsize=20);
        plt.xlabel('x', fontsize=20);

    def plt_3d(self, A, f1, f2, f3, Labels, l, title):
        colors = np.array(list(islice(cycle(['#377eb8', '#ff7f00', '#4daf4a',
                                             '#f781bf', '#a65628', '#984ea3',
                                             '#999999', '#e41a1c', '#dede00', '#000000']), 10)));

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.set_title(title)
        ax.set_ylabel("y")
        ax.set_xlabel("x")
        ax.set_zlabel("z")
        fig = plt.gcf()
        fig.canvas.set_window_title("clustring by " + title + " algorithm(3D)");
        for i in range(0, len(l)):
            ax.scatter(A[i][0], A[i][1], A[i][2], '.', color=colors[Labels[i]], s=5)
        return ax

    def clustring_kmeans(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs)
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()))

        A = np.array(l)

        kmeans = sklearn.cluster.KMeans(n_clusters=n)
        kmeans.fit(A)
        Centroids = kmeans.cluster_centers_
        Labels = kmeans.labels_

        if (dem == 2):
            self.plt_2d(A, 0, 1, Labels, "KMeans");
            plt.scatter(Centroids[:, 0], Centroids[:, 1], marker="x", s=100)
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, 0, 1, 2, Labels, l, "KMeans").scatter(Centroids[:, 0], Centroids[:, 1], Centroids[:, 2],
                                                                 marker="x", s=100, c="black");
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
            self.plt_2d(A, 0, 1, Labels, "MiniBatchKMeans");
            plt.scatter(Centroids[:, 0], Centroids[:, 1], marker="x", s=100)
            plt.show()

        elif (dem == 3):
            self.plt_3d(A, 0, 1, 2, Labels, l, "MiniBatchKMeans").scatter(Centroids[:, 0], Centroids[:, 1],
                                                                          Centroids[:, 2], marker="x", s=100,
                                                                          c="black");
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
            self.plt_2d(A, 0, 1, Labels, "Agglomerative");
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, 0, 1, 2, Labels, l, "Agglomerative");
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
            self.plt_2d(A, 0, 1, Labels, "Spectral");
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, 0, 1, 2, Labels, l, "Spectral");
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
            self.plt_2d(A, 0, 1, Labels, "Birch");
            plt.show()
        elif (dem == 3):
            self.plt_3d(A, 0, 1, 2, Labels, l, "Birch")
            plt.show()
        else:
            print("dem bad value");

    def clustring_cmeans(self, dem, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));
        A = np.array(l);

        colors = ['b', 'orange', 'g', 'r', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']

        xpts = np.array([]);
        ypts = np.array([]);
        zpts = np.array([]);
        for i in range(0, len(l)):
            ll = []
            ll.append(l[i][0]);
            xpts = np.append(xpts, ll.copy());
            ll = []
            ll.append(l[i][1]);
            ypts = np.append(ypts, ll.copy());
            ll = []
            ll.append(l[i][2]);
            zpts = np.append(zpts, ll.copy());
        if (dem == 2):
            alldata = np.vstack((xpts, ypts))
        elif (dem == 3):
            alldata = np.vstack((xpts, ypts, zpts));
        else:
            print("dem bad value");
        fpcs = []
        cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(alldata, n, 4, error=0.005, maxiter=1000, init=None)
        fpcs.append(fpc)
        cluster_membership = np.argmax(u, axis=0)

        if (dem == 2):
            for j in range(n):
                plt.plot(xpts[cluster_membership == j], ypts[cluster_membership == j], '.', color=colors[j],
                         markersize=5)
            plt.scatter(cntr[:, 0], cntr[:, 1], marker="x", s=100)
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
                        '.', color=colors[j], markersize=5)
            ax.scatter(cntr[:, 0], cntr[:, 1], cntr[:, 2], marker="x", s=100)
        else:
            print("dem bad value");
        plt.show();

    def clustring_mixture_gaussian(self, listOfMotifs, n):
        self.fill_dataSet(listOfMotifs);
        l = []
        for rec in self.data_set:
            l.append(list(rec.values()));

        A = np.array(l);
        t = A[0:89, 0:2]
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
                plt.plot(A[class_members, 0], A[class_members, 1], col + '.')
                plt.plot(cluster_center[0], cluster_center[1], markerfacecolor=col,
                         markeredgecolor='k', markersize=14)
                for x in A[class_members]:
                    plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
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
                ax.scatter(A[class_members, 0], A[class_members, 1], A[class_members, 2], '.', s=7)
                for x in A[class_members]:
                    plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], [cluster_center[2], x[2]], col)
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

        colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
        if (dem == 2):
            plt.title("MeanShift\nEstimated number of clusters: " + str(n_clusters_));
            fig = plt.gcf()
            fig.canvas.set_window_title("clustring by MeanShift algorithm(2D)");
            plt.ylabel('y', fontsize=20);
            plt.xlabel('x', fontsize=20);

            for k, col in zip(range(n_clusters_), colors):
                my_members = labels == k
                cluster_center = cluster_centers[k]
                plt.plot(A[my_members, 0], A[my_members, 1], col + '.')
                plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
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

            for k, col in zip(range(n_clusters_), colors):
                class_members = labels == k
                cluster_center = cluster_centers[k]
                ax.scatter(A[class_members, 0], A[class_members, 1], A[class_members, 2], '.', s=7)
                ax.scatter(cluster_center[0], cluster_center[1], cluster_center[2], 'o', color='k')
            plt.show()
        else:
            print("dem bad value");
        plt.show()


#f = Motif('E:\MY CODES\PYTHON\DNA-Toolkit\IMPORT-FILES\ebola.fasta',
          #'E:\MY CODES\PYTHON\DNA-Toolkit\IMPORT-FILES\motif_count.xlsx')
#ll = ["A", "G", "GAC", "GGGA", "GAGA", "AACCC", "GACGA", "CCAGT", "GGCCA", "CGCAG", "CTCTA", "AACGG"]
#f.clustring_meanshift(3, ll)



