# Uses python2
from __future__ import print_function
import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')

def optimal_points_old(segments):
    points = []
    #write your code here

    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

def optimal_points(segments):

    sorted_segments = sorted(segments, key=lambda x: (x.start, [(ord(c) for c in x.end)]))
    points = []
    while sorted_segments:
        # Place the first point to the right endpoint of the first segment.
        # Remove the segment, since it's considered as covered one.
        segment = sorted_segments.pop(0)
        point = segment.end
        points.append(point)

        # Check whether the point hit the other segments.
        for s in sorted_segments[:]:
            if s.start <= point <= s.end:
                sorted_segments.remove(s)

    return points

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, data = map(int, input.split())
    # segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    # points = optimal_points(segments)
    # print(len(points))
    # for p in points:
    #     print(p)

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[2:(2 * n + 2):2], data[3:(2 * n + 2):2])))
    print(segments)
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p,end=" ")

