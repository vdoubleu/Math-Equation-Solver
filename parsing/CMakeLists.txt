cmake_minimum_required(VERSION 3.10)  # CMake version check
project(build)               # Create project "simple_example"
set(CMAKE_CXX_STANDARD 14)            # Enable c++14 standard

# Add main.cpp file of project root directory as source file
set(SOURCE_FILES helloworld.cpp)

include_directories(amalgamate)

add_executable(MyExec
   amalgamate/crow_all.h)


# Add executable target with source files listed in SOURCE_FILES variable
add_executable(build ${SOURCE_FILES})
#SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -pthread")
#find_package(Threads REQUIRED)
#target_link_libraries(${PROJECT_NAME} ${Boost_LIBRARIES} ${CMAKE_THREAD_LIBS_INIT})


