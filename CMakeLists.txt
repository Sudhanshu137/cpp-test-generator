cmake_minimum_required(VERSION 3.10)
project(MyTestProject)

set(CMAKE_CXX_STANDARD 17)

# Ensure GoogleTest uses the dynamic runtime to match your app
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Include directories
include_directories(${PROJECT_SOURCE_DIR})
include_directories(googletest/googletest/include)

# Add GoogleTest
add_subdirectory(googletest)

# Correct source file globbing
file(GLOB SOURCES "input/*.cpp")   # ✅ Fix: input/input.cpp
file(GLOB TESTS "tests/*.cpp")

# Build the test runner
add_executable(test_runner ${SOURCES} ${TESTS})

# Link GoogleTest
target_link_libraries(test_runner gtest gtest_main)
