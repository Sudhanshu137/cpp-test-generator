// tests/input_test.cpp
#include <gtest/gtest.h>
#include "input.h" 


TEST(AddTest, PositiveNumbers) {
    EXPECT_EQ(add(2, 3), 5);
}

TEST(MultiplyTest, BasicTest) {
    EXPECT_EQ(multiply(3, 4), 12);
}
