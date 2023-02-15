import random
import time

import matplotlib.pyplot as plt
from scipy.spatial import distance

def assign_points_into_clusters(clusters_x, clusters_y, x_values, y_values):
    for i in range(0, len(x_values)):
        a = (x_values[i], y_values[i])
        b = (clusters_x[0][0], clusters_y[0][0])

        min = distance.euclidean(a, b)
        index = 0

        for j in range(1, len(clusters_x)):
            b = (clusters_x[j][0], clusters_y[j][0])
            actual_distance = distance.euclidean(a, b)
            if (actual_distance < min):
                min = actual_distance
                index = j

        for j in range(0, len(clusters_x)):
            if (index == j):
                clusters_x[j].append(x_values[i])
                clusters_y[j].append(y_values[i])

    return clusters_x, clusters_y

def print_average_points_distance(clusters_x, clusters_y, choice, print_or_not):
    big_sum = 0
    sums = []
    for i in range(0, len(clusters_x)):
        x_average = 0
        y_average = 0

        for j in range(1, len(clusters_x[i])):
            x_average = x_average + clusters_x[i][j]
            y_average = y_average + clusters_y[i][j]

        x_average = x_average / len(clusters_x[i])
        y_average = y_average / len(clusters_y[i])

        a = (x_average, y_average)

        sum = 0
        for j in range(1, len(clusters_x[i])):
            b = (clusters_x[i][j], clusters_y[i][j])
            sum = sum + (distance.euclidean(a, b))

        sum = sum / len(clusters_x[i])

        sums.append(sum)
        big_sum = big_sum + sum

        if(print_or_not == 'p'):
            print(sum)

    big_sum = big_sum / len(clusters_x)
    if(print_or_not == 'p'):
        print("SUM = ", big_sum)
        print("------------------")

    if(choice == 'd'):
        return sums.index(max(sums))

    if(choice == 's'):
        return sums

    else:
        return big_sum

def show_plot(clusters_x, clusters_y, len_clusters):

    for i in range(0, len_clusters):
        plt.scatter(clusters_x[i][1:], clusters_y[i][1:], 1)

    plt.show()

def get_first_20_centroids(x_values, y_values):
    centroids = []
    x = []
    y = []

    while (len(x) < 15 and len(y) < 15):
        x_randoms = range(-5000, 5000)
        x_axis = random.sample(x_randoms, 1)

        y_randoms = range(-5000, 5000)
        y_axis = random.sample(y_randoms, 1)

        pom = 0
        for i in range(0, len(x)):
            if((x[i] != x_axis[0] and y[i] != y_axis[0]) or (x[i] == x_axis[0] and y[i] != y_axis[0]) or (x[i] != x_axis[0] and y[i] == y_axis[0])):
                continue
            if(x[i] == x_axis[0] and y[i] == y_axis[0]):
                pom = 1
                break

        if(pom == 0):
            x.append(x_axis[0])
            y.append(y_axis[0])
            continue
        else:
            continue


    centroids.append(x)
    centroids.append(y)

    return x, y

def get_2_centroids(x_max, x_min, y_max, y_min):
    centroids = []
    x = []
    y = []

    while (len(x) < 2 and len(y) < 2):
        x_randoms = range(x_min, x_max)
        x_axis = random.sample(x_randoms, 1)

        y_randoms = range(y_min, y_max)
        y_axis = random.sample(y_randoms, 1)

        pom = 0
        for i in range(0, len(x)):
            if ((x[i] != x_axis[0] and y[i] != y_axis[0]) or (x[i] == x_axis[0] and y[i] != y_axis[0]) or (
                    x[i] != x_axis[0] and y[i] == y_axis[0])):
                continue
            if (x[i] == x_axis[0] and y[i] == y_axis[0]):
                pom = 1
                break

        if (pom == 0):
            x.append(x_axis[0])
            y.append(y_axis[0])
            continue
        else:
            continue

    centroids.append(x)
    centroids.append(y)

    return x, y

def assign_points_to_centroids(centroids_x, centroids_y, x, y, value):
    clusters_x = [[centroids_x[0]], [centroids_x[1]]] #, [centroids_x[2]], [centroids_x[3]], [centroids_x[4]],
                  # [centroids_x[5]], [centroids_x[6]], [centroids_x[7]], [centroids_x[8]], [centroids_x[9]],
                  # [centroids_x[10]], [centroids_x[11]], [centroids_x[12]], [centroids_x[13]], [centroids_x[14]]]
                  # [centroids_x[15]], [centroids_x[16]], [centroids_x[17]], [centroids_x[18]], [centroids_x[19]]]
                  # [centroids_x[20]], [centroids_x[21]], [centroids_x[22]], [centroids_x[23]], [centroids_x[24]],
                  # [centroids_x[25]], [centroids_x[26]], [centroids_x[27]], [centroids_x[28]], [centroids_x[29]]]


    clusters_y = [[centroids_y[0]], [centroids_y[1]]] #, [centroids_y[2]], [centroids_y[3]], [centroids_y[4]],
                  # [centroids_y[5]], [centroids_y[6]], [centroids_y[7]], [centroids_y[8]], [centroids_y[9]],
                  # [centroids_y[10]], [centroids_y[11]], [centroids_y[12]], [centroids_y[13]], [centroids_y[14]]]
                  # [centroids_y[15]], [centroids_y[16]], [centroids_y[17]], [centroids_y[18]], [centroids_y[19]]]
                  # [centroids_y[20]], [centroids_y[21]], [centroids_y[22]], [centroids_y[23]], [centroids_y[24]],
                  # [centroids_y[25]], [centroids_y[26]], [centroids_y[27]], [centroids_y[28]], [centroids_y[29]]]


    # BEFORE
    clusters_x, clusters_y = assign_points_into_clusters(clusters_x, clusters_y, x, y)

    if(value == 'k'):
        print_average_points_distance(clusters_x, clusters_y, 'k', 'p')
        show_plot(clusters_x, clusters_y, len(clusters_x))

    # AFTER
    sums = []
    for m in range(0,100):
        for i in range(0, len(clusters_x)):
            xx = 0
            yy = 0

            for j in range(1, len(clusters_x[i])):
                xx = xx + clusters_x[i][j]
                yy = yy + clusters_y[i][j]

            average_x = xx / len(clusters_x[i])
            average_y = yy / len(clusters_y[i])

            clusters_x[i][0] = average_x
            clusters_y[i][0] = average_y

        for i in range(0,len(clusters_x)):
            del clusters_x[i][1:]
            del clusters_y[i][1:]

        clusters_x, clusters_y = assign_points_into_clusters(clusters_x, clusters_y, x, y)

        if (value == 'k'):
            big_sum = print_average_points_distance(clusters_x, clusters_y, 'k', 'p')
        else:
            pom = ''
            big_sum = print_average_points_distance(clusters_x, clusters_y, 'k', pom)

        sums.append(big_sum)

        if(m > 0):
            if(int(sums[m]) == int(sums[m-1])):
                break

    if (value == 'k'):
        show_plot(clusters_x, clusters_y, len(clusters_x))

    return clusters_x, clusters_y

def get_medoids(x_values, y_values, number):
    x = []
    y = []


    randoms = range(0, len(x_values))
    my_random = random.sample(randoms, number)
    for j in range(0, len(x_values)):
        for m in range(0, len(my_random)):
            if(j == my_random[m]):
                x.append(x_values[j])
                y.append(y_values[j])

    # print(x)
    # print(y)

    return x, y

def assign_points_to_medoids(medoids_x, medoids_y, x, y, value):
    clusters_x = [[medoids_x[0]], [medoids_x[1]], [medoids_x[2]], [medoids_x[3]], [medoids_x[4]],
                  [medoids_x[5]], [medoids_x[6]], [medoids_x[7]], [medoids_x[8]], [medoids_x[9]],
                  [medoids_x[10]], [medoids_x[11]], [medoids_x[12]], [medoids_x[13]], [medoids_x[14]]]
                  # [medoids_x[15]], [medoids_x[16]], [medoids_x[17]], [medoids_x[18]], [medoids_x[19]]]
                  # [medoids_x[20]], [medoids_x[21]], [medoids_x[22]], [medoids_x[23]], [medoids_x[24]],
                  # [medoids_x[25]], [medoids_x[26]], [medoids_x[27]], [medoids_x[28]], [medoids_x[29]]]

    clusters_y = [[medoids_y[0]], [medoids_y[1]], [medoids_y[2]], [medoids_y[3]], [medoids_y[4]],
                  [medoids_y[5]], [medoids_y[6]], [medoids_y[7]], [medoids_y[8]], [medoids_y[9]],
                  [medoids_y[10]], [medoids_y[11]], [medoids_y[12]], [medoids_y[13]], [medoids_y[14]]]
                  # [medoids_y[15]], [medoids_y[16]], [medoids_y[17]], [medoids_y[18]], [medoids_y[19]]]
                  # [medoids_y[20]], [medoids_y[21]], [medoids_y[22]], [medoids_y[23]], [medoids_y[24]],
                  # [medoids_y[25]], [medoids_y[26]], [medoids_y[27]], [medoids_y[28]], [medoids_y[29]]]


    # BEFORE
    clusters_x, clusters_y = assign_points_into_clusters(clusters_x, clusters_y, x, y)

    if(value == 'k'):
        print_average_points_distance(clusters_x, clusters_y, 'k', 'p')
        show_plot(clusters_x, clusters_y, len(clusters_x))


    # AFTER
    sums = []
    for m in range(0,100):
        for i in range(0, len(clusters_x)):
            xx = 0
            yy = 0

            for j in range(1, len(clusters_x[i])):
                xx = xx + clusters_x[i][j]
                yy = yy + clusters_y[i][j]

            average_x = xx / len(clusters_x[i])
            average_y = yy / len(clusters_y[i])

            a = (average_x, average_y)
            b = (clusters_x[i][1], clusters_y[i][1])
            dist = distance.euclidean(a, b)
            min = dist
            index = 0
            for j in range(2, len(clusters_x[i])):
                b = (clusters_x[i][j], clusters_y[i][j])
                dist = distance.euclidean(a, b)

                if (dist < min):
                    min = dist
                    index = j

            clusters_x[i][0] = clusters_x[i][index]
            clusters_y[i][0] = clusters_y[i][index]

        for i in range(0,len(clusters_x)):
            del clusters_x[i][1:]
            del clusters_y[i][1:]

        assign_points_into_clusters(clusters_x, clusters_y, x, y)


        if (value == 'k'):
            big_sum = print_average_points_distance(clusters_x, clusters_y, 'k', 'p')
        else:
            pom = ''
            big_sum = print_average_points_distance(clusters_x, clusters_y, 'k', pom)

        sums.append(big_sum)

        if(m > 0):
            if(int(sums[m]) == int(sums[m-1])):
                break

    if(value == 'k'):
        show_plot(clusters_x, clusters_y, len(clusters_x))

    return clusters_x, clusters_y

def create_points(menu):
    x_randoms = range(-5000, 5000)
    x = random.sample(x_randoms, 20)

    y_randoms = range(-5000, 5000)
    y = random.sample(y_randoms, 20)

    # print(x)
    # print(y)


    for i in range(0, 40000):
        # get random x
        randoms = range(0, len(x))
        my_random = random.sample(randoms,1)

        for j in range (0,len(x)):
            if(j == my_random[0]):
                new_x = x[j]
                x_offset = range(-100, 100)
                get_offset_x = random.sample(x_offset, 1)
                new_x = new_x + get_offset_x[0]
                x.append(new_x)

                new_y = y[j]
                y_offset = range(-100, 100)
                get_offset_y = random.sample(y_offset, 1)
                new_y = new_y + get_offset_y[0]
                y.append(new_y)
                break



    if(menu == '1'):
        centroids_x, centroids_y = get_first_20_centroids(x, y)

        print(centroids_x)
        print(centroids_y)

        assign_points_to_centroids(centroids_x, centroids_y, x, y, 'k')

        return

    if(menu == '2'):
        medoids_x, medoids_y = get_medoids(x, y, 20)

        assign_points_to_medoids(medoids_x, medoids_y, x, y, 'k')

        return

    if(menu == '3'):
        division_clustering(x, y)

def division_clustering(x_values, y_values):
    clusters_x = []
    clusters_y = []

    first_cluster_x = []
    first_cluster_y = []

    second_cluster_x = []
    second_cluster_y = []

    for i in range(0, len(x_values)):
        if(-5000 < x_values[i] < 0):
            first_cluster_x.append(x_values[i])
            first_cluster_y.append(y_values[i])
        if(0 < x_values[i] < 5000):
            second_cluster_x.append(x_values[i])
            second_cluster_y.append(y_values[i])

    clusters_x.append(first_cluster_x)
    clusters_x.append(second_cluster_x)
    clusters_y.append(first_cluster_y)
    clusters_y.append(second_cluster_y)

    # FIRST ASSIGN POINTS
    for i in range(0, len(clusters_x)):
        xx = 0
        yy = 0

        for j in range(1, len(clusters_x[i])):
            xx = xx + clusters_x[i][j]
            yy = yy + clusters_y[i][j]

        average_x = xx / len(clusters_x[i])
        average_y = yy / len(clusters_y[i])

        clusters_x[i][0] = average_x
        clusters_y[i][0] = average_y

        for i in range(0, len(clusters_x)):
            del clusters_x[i][1:]
            del clusters_y[i][1:]

        clusters_x, clusters_y = assign_points_into_clusters(clusters_x, clusters_y, x_values, y_values)

    # LOOP ASSIGN POINTS
    for m in range(0,100):
        pom = ''
        maximum = print_average_points_distance(clusters_x, clusters_y, 'd', pom )

        if(m == 0):
            show_plot(clusters_x, clusters_y, len(clusters_x))

        x_min = min(clusters_x[maximum])
        x_max = max(clusters_x[maximum])
        y_min = min(clusters_y[maximum])
        y_max = max(clusters_y[maximum])

        centroids_x, centroids_y = get_2_centroids(x_max, x_min, y_max, y_min)

        new_centroids_x, new_centroids_y = assign_points_to_centroids(centroids_x, centroids_y, clusters_x[maximum], clusters_y[maximum], 'd')

        del clusters_x[maximum]
        del clusters_y[maximum]

        for i in range(0, len(clusters_x)):
            del clusters_x[i][1:]
            del clusters_y[i][1:]

        for i in range(0,2):
            clusters_x.append(new_centroids_x[i])
            clusters_y.append(new_centroids_y[i])

        clusters_x, clusters_y = assign_points_into_clusters(clusters_x, clusters_y, x_values, y_values)

        sums = print_average_points_distance(clusters_x, clusters_y, 's', 'p')

        the_500 = 0
        for i in range(0,len(sums)):
            if(sums[i] > 500):
                the_500 = 1
                break

        if(the_500 == 0):
            print("This are final clusters !")
            show_plot(clusters_x, clusters_y, len(clusters_x))
            break

        show_plot(clusters_x, clusters_y, len(clusters_x))

menu = input("Vyber si moznost: \n"
      "1 --> k-means, centroid\n"
      "2 --> k-means, medoid\n"
      "3 --> divizne zhlukovanie, stred je centroid\n")

if(menu == '1'):
    start_time = time.time()
    create_points(menu)
    end_time = time.time()
    print("Time: %s" %(end_time - start_time), "seconds")
if(menu == '2'):
    start_time = time.time()
    create_points(menu)
    end_time = time.time()
    print("Time: %s" % (end_time - start_time), "seconds")
if(menu == '3'):
    start_time = time.time()
    create_points(menu)
    end_time = time.time()
    print("Time: %s" % (end_time - start_time), "seconds")

