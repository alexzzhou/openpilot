#include "messaging.h"
#include "impl_zmq.h"
#include "impl_msgq.h"

#ifdef __APPLE__
const bool MUST_USE_ZMQ = true;
#else
const bool MUST_USE_ZMQ = false;
#endif

bool messaging_use_zmq(){
  return std::getenv("ZMQ") || MUST_USE_ZMQ || true;
}

Context * Context::create(){
  Context * c;
  if (messaging_use_zmq()){
    c = new ZMQContext();
  } else {
    c = new MSGQContext();
  }
  return c;
}

Context * Context::create(bool use_zmq){
  Context * c;
  if (use_zmq || messaging_use_zmq()){
    c = new ZMQContext();
  } else {
    c = new MSGQContext();
  }
  return c;
}

SubSocket * SubSocket::create(){
  SubSocket * s;
  if (messaging_use_zmq()){
    s = new ZMQSubSocket();
  } else {
    s = new MSGQSubSocket();
  }
  return s;
}

SubSocket * SubSocket::create(bool use_zmq){
  SubSocket * s;
  if (use_zmq || messaging_use_zmq()){
    s = new ZMQSubSocket();
  } else {
    s = new MSGQSubSocket();
  }
  return s;
}

/*
SubSocket * SubSocket::create(Context * context, std::string endpoint, std::string address, bool conflate, bool check_endpoint){
  SubSocket *s = SubSocket::create();
  int r = s->connect(context, endpoint, address, conflate, check_endpoint);

  if (r == 0) {
    return s;
  } else {
    delete s;
    return NULL;
  }
}
*/

SubSocket * SubSocket::create(Context * context, std::string endpoint, std::string address, bool conflate, bool check_endpoint, bool use_zmq){
  SubSocket *s = SubSocket::create(use_zmq);
  int r = s->connect(context, endpoint, address, conflate, check_endpoint);

  if (r == 0) {
    return s;
  } else {
    delete s;
    return NULL;
  }
}

PubSocket * PubSocket::create(){
  PubSocket * s;
  if (messaging_use_zmq()){
    s = new ZMQPubSocket();
  } else {
    s = new MSGQPubSocket();
  }
  return s;
}

PubSocket * PubSocket::create(bool use_zmq){
  PubSocket * s;
  if (use_zmq || messaging_use_zmq()){
    s = new ZMQPubSocket();
  } else {
    s = new MSGQPubSocket();
  }
  return s;
}

/*
PubSocket * PubSocket::create(Context * context, std::string endpoint, bool check_endpoint){
  PubSocket *s = PubSocket::create();
  int r = s->connect(context, endpoint, check_endpoint);

  if (r == 0) {
    return s;
  } else {
    delete s;
    return NULL;
  }
}
*/

PubSocket * PubSocket::create(Context * context, std::string endpoint, bool check_endpoint, bool use_zmq){
  PubSocket *s = PubSocket::create(use_zmq);
  int r = s->connect(context, endpoint, check_endpoint);

  if (r == 0) {
    return s;
  } else {
    delete s;
    return NULL;
  }
}

Poller * Poller::create(){
  Poller * p;
  if (messaging_use_zmq()){
    p = new ZMQPoller();
  } else {
    p = new MSGQPoller();
  }
  return p;
}

Poller * Poller::create(bool use_zmq){
  Poller * p;
  if (use_zmq || messaging_use_zmq()){
    p = new ZMQPoller();
  } else {
    p = new MSGQPoller();
  }
  return p;
}

Poller * Poller::create(std::vector<SubSocket*> sockets){
  Poller * p = Poller::create();

  for (auto s : sockets){
    p->registerSocket(s);
  }
  return p;
}

Poller * Poller::create(std::vector<SubSocket*> sockets, bool use_zmq){
  Poller * p = Poller::create(use_zmq);

  for (auto s : sockets){
    p->registerSocket(s);
  }
  return p;
}

extern "C" Context * messaging_context_create() {
  return Context::create();
}

extern "C" SubSocket * messaging_subsocket_create(Context* context, const char* endpoint) {
  return SubSocket::create(context, std::string(endpoint));
}

extern "C" PubSocket * messaging_pubsocket_create(Context* context, const char* endpoint) {
  return PubSocket::create(context, std::string(endpoint));
}

extern "C" Poller * messaging_poller_create(SubSocket** sockets, int size) {
  std::vector<SubSocket*> socketsVec(sockets, sockets + size);
  return Poller::create(socketsVec);
}
