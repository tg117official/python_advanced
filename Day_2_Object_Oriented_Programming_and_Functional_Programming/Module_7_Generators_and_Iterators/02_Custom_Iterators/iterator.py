################################## BASIC ###############################################

# Exercise 1: Create a custom iterator for a sequence
# Problem: Implement a custom iterator `MyRange` that behaves like `range` but takes a start, stop, and step.
# Relevance: Custom iterators allow tailored iteration behavior, common in applications like custom pagination.
class MyRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

print("Exercise 1 Result:", list(MyRange(1, 10, 2)))  # Output: [1, 3, 5, 7, 9]

# Exercise 2: Reverse iterator
# Problem: Create an iterator `ReverseIterator` that iterates over a sequence in reverse.
# Relevance: Reverse iteration is useful for data processing tasks like undo operations or backtracking.
class ReverseIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = len(sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.sequence[self.index]

print("\nExercise 2 Result:", list(ReverseIterator([1, 2, 3, 4, 5])))  # Output: [5, 4, 3, 2, 1]

# Exercise 3: Cycling iterator
# Problem: Implement an iterator `CyclingIterator` that cycles through a sequence indefinitely.
# Relevance: Cycling iterators are commonly used in round-robin scheduling or repeated tasks.
class CyclingIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sequence:
            raise StopIteration
        value = self.sequence[self.index]
        self.index = (self.index + 1) % len(self.sequence)
        return value

cycle_iter = CyclingIterator([1, 2, 3])
print("\nExercise 3 Result:", [next(cycle_iter) for _ in range(7)])
# Output: [1, 2, 3, 1, 2, 3, 1]

# Exercise 4: Pair iterator
# Problem: Write an iterator `PairIterator` that iterates over pairs of adjacent elements.
# Relevance: Useful in tasks like comparing consecutive elements in data analysis.
class PairIterator:
    def __init__(self, sequence):
        self.sequence = sequence
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence) - 1:
            raise StopIteration
        pair = (self.sequence[self.index], self.sequence[self.index + 1])
        self.index += 1
        return pair

print("\nExercise 4 Result:", list(PairIterator([1, 2, 3, 4])))
# Output: [(1, 2), (2, 3), (3, 4)]

# Exercise 5: Infinite iterator
# Problem: Implement an iterator `InfiniteCounter` that generates numbers starting from a given value indefinitely.
# Relevance: Common in applications requiring unbounded sequences, like generating unique IDs.
class InfiniteCounter:
    def __init__(self, start=0):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += 1
        return value

infinite = InfiniteCounter(10)
print("\nExercise 5 Result:", [next(infinite) for _ in range(5)])  # Output: [10, 11, 12, 13, 14]

# Exercise 6: Limited repeat iterator
# Problem: Create an iterator `RepeatIterator` that repeats an item a specified number of times.
# Relevance: Useful in simulations or testing scenarios requiring repetitive data.
class RepeatIterator:
    def __init__(self, value, times):
        self.value = value
        self.times = times
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.times:
            raise StopIteration
        self.count += 1
        return self.value

print("\nExercise 6 Result:", list(RepeatIterator("A", 4)))  # Output: ['A', 'A', 'A', 'A']

# Exercise 7: Range iterator with skip logic
# Problem: Implement `SkipIterator` that skips every nth element in a range.
# Relevance: Useful for filtering specific patterns in data streams.
class SkipIterator:
    def __init__(self, sequence, skip_step):
        self.sequence = sequence
        self.skip_step = skip_step
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        value = self.sequence[self.index]
        self.index += self.skip_step
        return value

print("\nExercise 7 Result:", list(SkipIterator([1, 2, 3, 4, 5, 6], 2)))  # Output: [1, 3, 5]

# Exercise 8: Grouping iterator
# Problem: Implement an iterator `GroupIterator` that groups elements into fixed-size chunks.
# Relevance: Often used in batch processing tasks in data engineering pipelines.
class GroupIterator:
    def __init__(self, sequence, group_size):
        self.sequence = sequence
        self.group_size = group_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        group = self.sequence[self.index:self.index + self.group_size]
        self.index += self.group_size
        return group

print("\nExercise 8 Result:", list(GroupIterator([1, 2, 3, 4, 5, 6], 2)))
# Output: [[1, 2], [3, 4], [5, 6]]

# Exercise 9: Circular buffer iterator
# Problem: Create a `CircularBuffer` iterator that behaves like a circular buffer for a fixed number of elements.
# Relevance: Widely used in real-time data streams or logging systems.
class CircularBuffer:
    def __init__(self, sequence, buffer_size):
        self.sequence = sequence
        self.buffer_size = buffer_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sequence:
            raise StopIteration
        value = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return value

buffer = CircularBuffer([1, 2, 3], 3)
print("\nExercise 9 Result:", [next(buffer) for _ in range(6)])
# Output: [1, 2, 3, 1, 2, 3]

# Exercise 10: Interleaving iterator
# Problem: Write an iterator `InterleaveIterator` that alternates elements from multiple iterables.
# Relevance: Useful for combining datasets for joint processing.
class InterleaveIterator:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.iterators = [iter(it) for it in iterables]

    def __iter__(self):
        return self

    def __next__(self):
        for iterator in self.iterators:
            try:
                return next(iterator)
            except StopIteration:
                self.iterators.remove(iterator)
        raise StopIteration

interleaved = InterleaveIterator([1, 2, 3], ['a', 'b', 'c'], ['X', 'Y'])
print("\nExercise 10 Result:", list(interleaved))
# Output: [1, 'a', 'X', 2, 'b', 'Y', 3, 'c']



############################### INTERMEDIATE ##############################################

# Exercise 1: Flatten a nested list using an iterator
# Problem: Create an iterator `FlattenIterator` to flatten a nested list.
# Relevance: Useful in processing hierarchical or nested data structures, common in JSON or XML parsing.
class FlattenIterator:
    def __init__(self, nested_list):
        self.stack = nested_list[::-1]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            item = self.stack.pop()
            if isinstance(item, list):
                self.stack.extend(item[::-1])
            else:
                return item
        raise StopIteration

nested_list = [1, [2, [3, 4], 5], 6]
print("Exercise 1 Result:", list(FlattenIterator(nested_list)))
# Output: [1, 2, 3, 4, 5, 6]

# Exercise 2: Chunked iterator with overlapping windows
# Problem: Implement an iterator `OverlappingChunkIterator` that yields overlapping chunks of a list.
# Relevance: Used in time-series analysis or signal processing.
class OverlappingChunkIterator:
    def __init__(self, sequence, chunk_size, overlap):
        self.sequence = sequence
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        start = self.index
        end = min(start + self.chunk_size, len(self.sequence))
        self.index += self.chunk_size - self.overlap
        return self.sequence[start:end]

data = [1, 2, 3, 4, 5, 6]
print("\nExercise 2 Result:", list(OverlappingChunkIterator(data, 3, 1)))
# Output: [[1, 2, 3], [3, 4, 5], [5, 6]]

# Exercise 3: Zigzag iterator for multiple lists
# Problem: Implement a `ZigzagIterator` that alternates between multiple iterables.
# Relevance: Useful for processing data from multiple sources in parallel.
class ZigzagIterator:
    def __init__(self, *iterables):
        self.iterables = [iter(it) for it in iterables]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iterables:
            raise StopIteration
        while True:
            current_iter = self.iterables[self.index]
            try:
                result = next(current_iter)
                self.index = (self.index + 1) % len(self.iterables)
                return result
            except StopIteration:
                self.iterables.pop(self.index)
                if not self.iterables:
                    raise StopIteration

iter1 = [1, 2, 3]
iter2 = ['a', 'b']
iter3 = [10, 20, 30]
print("\nExercise 3 Result:", list(ZigzagIterator(iter1, iter2, iter3)))
# Output: [1, 'a', 10, 2, 'b', 20, 3, 30]

# Exercise 4: Limited infinite iterator
# Problem: Create an iterator `LimitedInfiniteIterator` that repeats a value up to a maximum count.
# Relevance: Useful in simulations or limited retries in distributed systems.
class LimitedInfiniteIterator:
    def __init__(self, value, max_count):
        self.value = value
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.value

print("\nExercise 4 Result:", list(LimitedInfiniteIterator('Hello', 5)))
# Output: ['Hello', 'Hello', 'Hello', 'Hello', 'Hello']

# Exercise 5: Filtering iterator
# Problem: Create an iterator `FilteringIterator` that only yields elements that satisfy a condition.
# Relevance: Used in data cleaning and filtering pipelines.
class FilteringIterator:
    def __init__(self, sequence, condition):
        self.sequence = iter(sequence)
        self.condition = condition

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self.sequence)
            if self.condition(value):
                return value

data = [10, 15, 20, 25, 30]
print("\nExercise 5 Result:", list(FilteringIterator(data, lambda x: x % 10 == 0)))
# Output: [10, 20, 30]

# Exercise 6: Transforming iterator
# Problem: Write an iterator `TransformingIterator` that applies a function to each element.
# Relevance: Common in data transformation tasks like scaling or formatting.
class TransformingIterator:
    def __init__(self, sequence, transform):
        self.sequence = iter(sequence)
        self.transform = transform

    def __iter__(self):
        return self

    def __next__(self):
        return self.transform(next(self.sequence))

data = [1, 2, 3, 4]
print("\nExercise 6 Result:", list(TransformingIterator(data, lambda x: x * x)))
# Output: [1, 4, 9, 16]

# Exercise 7: Paired iterator
# Problem: Implement an iterator `PairwiseIterator` that yields pairs of consecutive elements.
# Relevance: Useful in detecting trends or changes in sequences.
class PairwiseIterator:
    def __init__(self, sequence):
        self.sequence = iter(sequence)
        self.prev = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.prev is None:
            self.prev = next(self.sequence)
        current = next(self.sequence)
        pair = (self.prev, current)
        self.prev = current
        return pair

data = [10, 20, 30, 40]
print("\nExercise 7 Result:", list(PairwiseIterator(data)))
# Output: [(10, 20), (20, 30), (30, 40)]

# Exercise 8: Skipping iterator
# Problem: Implement an iterator `SkippingIterator` that skips every nth element.
# Relevance: Used in downsampling data streams.
class SkippingIterator:
    def __init__(self, sequence, skip_step):
        self.sequence = iter(sequence)
        self.skip_step = skip_step
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = next(self.sequence)
        self.count += 1
        if self.count == self.skip_step:
            self.count = 0
            return self.__next__()
        return value

data = [1, 2, 3, 4, 5, 6]
print("\nExercise 8 Result:", list(SkippingIterator(data, 3)))
# Output: [1, 2, 4, 5]

# Exercise 9: Random sampling iterator
# Problem: Create an iterator `RandomSampleIterator` that yields random samples from a sequence.
# Relevance: Used in random testing or sampling for analytics.
import random
class RandomSampleIterator:
    def __init__(self, sequence, sample_size):
        self.sequence = sequence
        self.sample_size = sample_size

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sequence or self.sample_size <= 0:
            raise StopIteration
        return random.choice(self.sequence)

random_samples = RandomSampleIterator([1, 2, 3, 4, 5], 3)
print("\nExercise 9 Result:", [next(random_samples) for _ in range(3)])
# Output: Random 3 numbers from the sequence

# Exercise 10: Chained iterator
# Problem: Implement an iterator `ChainedIterator` that combines multiple sequences.
# Relevance: Used for merging multiple datasets in sequence.
class ChainedIterator:
    def __init__(self, *sequences):
        self.iterators = [iter(seq) for seq in sequences]

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterators:
            try:
                return next(self.iterators[0])
            except StopIteration:
                self.iterators.pop(0)
        raise StopIteration

print("\nExercise 10 Result:", list(ChainedIterator([1, 2], ['a', 'b'], [10, 20])))
# Output: [1, 2, 'a', 'b', 10, 20]
