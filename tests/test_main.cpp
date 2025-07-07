
// test_input.cpp
#include <gtest/gtest.h>
#include "input.h"

TEST(InputTest, Addition) {
  ASSERT_EQ(add(2,3), 5);
}

TEST(InputTest, Multiplication) {
  ASSERT_EQ(multiply(4,5), 20);
}

