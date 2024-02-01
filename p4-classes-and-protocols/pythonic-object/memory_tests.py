from vector2D import Vector2D as Vector2D_without_slots
from vector2D_slots import Vector2D as Vector2D_with_slots
import sys
import time
import resource
import tracemalloc
import os


def memory_test(module_name, vector_class, n=10 ** 5):
    perf_data = {}
    tracemalloc.start()
    t0 = time.perf_counter()
    mem0 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    v = [vector_class(i, i) for i in range(10 ** 5)]
    t1 = time.perf_counter()
    mem1 = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    perf_data["module_name"] = module_name
    perf_data["vector_class"] = vector_class
    perf_data["time"] = str(t1 - t0) + " s"
    perf_data["initial_memory"] = str(mem0) + " KB"
    perf_data["final_memory"] = str(mem1) + " KB"
    perf_data["memory_diff"] = str(mem1 - mem0) + " KB"
    perf_data["current_memory"] = str(current / 1024) + " KB"
    perf_data["peak_memory"] = str(peak / 1024) + " KB"

    # save the data in a file
    with open("./data/" + module_name + "-memory_test.txt", "w") as f:
        f.write("Performance data for module " + module_name + " by creating " + str(
            n) + " instances of class " + vector_class.__name__ + "\n")
        f.write("\n")
        f.write("metric" + " " * 13 + "| value\n")
        f.write("-" * 60 + "\n")
        for key in perf_data:
            print(key, perf_data[key])
            f.write(key + " " * (19 - len(key)) + "| " + str(perf_data[key]) + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python memory_tests.py <module_name> <n>")
        exit(1)

    if len(sys.argv) == 3:
        module_name = sys.argv[1]
        n = int(sys.argv[2])
        if module_name == "vector2D":
            memory_test(module_name, Vector2D_without_slots, n)
        elif module_name == "vector2D_slots":
            memory_test(module_name, Vector2D_with_slots, n)
        else:
            print("module name must be either vector2D or vector2D_slots")
            exit(1)
    elif len(sys.argv) == 4:
        module_name1 = sys.argv[1]
        module_name2 = sys.argv[2]
        n = int(sys.argv[3])
        if module_name1 == "vector2D":
            memory_test(module_name1, Vector2D_without_slots, n)
        if module_name2 == "vector2D_slots":
            memory_test(module_name2, Vector2D_with_slots, n)
    print("done")
