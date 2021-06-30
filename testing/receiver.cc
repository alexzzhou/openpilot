#include <iostream>
#include <cstddef>
#include <chrono>
#include <thread>
#include <cassert>

#include "/data/openpilot/cereal/messaging/messaging.h"
#include "/data/openpilot/cereal/messaging/impl_zmq.h"

#define MSGS 100

int main() {
  Context * csub = Context::create();
  SubSocket * sub_sock = SubSocket::create(csub, "controlsState", "127.0.0.1", false, true, true);
}