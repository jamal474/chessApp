cmake_minimum_required(VERSION 3.10)
project(chess-cpp-s)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Collect all source and header files
set(SOURCES
    main.cpp
    Server.cpp
    Board.cpp
    Bishop.cpp
    Chess_Piece.cpp
    Conn_handler.cpp
    Game.cpp
    GlobalDefinitions.cpp
    King.cpp
    Knight.cpp
    Pawn.cpp
    Player.cpp
    Queen.cpp
    Rook.cpp
)

set(HEADERS
    Server.h
    Board.h
    Bishop.h
    Chess_Piece.h
    Conn_handler.h
    Game.h
    GlobalDefinitions.h
    King.h
    Knight.h
    Pawn.h
    Player.h
    Queen.h
    Rook.h
)

# Add executable including both source and header files
add_executable(CppServer ${SOURCES} ${HEADERS})

# Specify Boost location if needed
set(BOOST_ROOT "/opt/homebrew/Cellar/boost/1.86.0_2/")
set(BOOST_INCLUDEDIR "/opt/homebrew/Cellar/boost/1.86.0_2/include")
set(BOOST_LIBRARYDIR "/opt/homebrew/Cellar/boost/1.86.0_2/lib")

# Find Boost libraries
find_package(Boost 1.86 REQUIRED COMPONENTS filesystem system)

if(Boost_FOUND)
    include_directories(${Boost_INCLUDE_DIRS})
    link_directories(${Boost_LIBRARY_DIRS})
else()
    message(FATAL_ERROR "Boost not found!")
endif()

# Link Boost libraries
target_link_libraries(CppServer Boost::filesystem Boost::system)

find_package(nlohmann_json REQUIRED)
target_link_libraries(CppServer nlohmann_json::nlohmann_json)
