cmake_minimum_required(VERSION 3.10)
project(chessStateServer)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

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

find_package(Boost REQUIRED COMPONENTS filesystem system)
find_package(nlohmann_json REQUIRED)

add_executable(CppServer ${SOURCES} ${HEADERS})

target_link_libraries(CppServer boost::boost)
target_link_libraries(CppServer nlohmann_json::nlohmann_json)
