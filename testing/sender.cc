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
  SubSocket * sub_sock = SubSocket::create(csub, "controlsState", "127.0.0.1", false, true, false);

  Context * cpub = Context::create(true);
  PubSocket * pub_sock = PubSocket::create(c, "controlsState", "127.0.0.1", false, true, true);

  char data[8];

  Poller * poller = Poller::create({sub_sock});

  auto start = std::chrono::steady_clock::now();

  for (uint64_t i = 0; i < MSGS; i++){
    *(uint64_t*)data = i;
    pub_sock->send(data, 8);

    auto r = poller->poll(100);

    for (auto p : r){
      Message * m = p->receive();
      uint64_t ii = *(uint64_t*)m->getData();
      assert(i == ii);
      delete m;
    }
  }

  while (true) {
    Message * m = p->receive();
  }


  auto end = std::chrono::steady_clock::now();
  double elapsed = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count() / 1e9;
  double throughput = ((double) MSGS / (double) elapsed);
  std::cout << throughput << " msg/s" << std::endl;

  delete poller;
  delete sub_sock;
  delete pub_sock;
  delete c;


  return 0;
}
