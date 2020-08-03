# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import buckets_pb2 as buckets__pb2


class APIStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_unary(
                '/buckets.pb.API/List',
                request_serializer=buckets__pb2.ListRequest.SerializeToString,
                response_deserializer=buckets__pb2.ListReply.FromString,
                )
        self.Init = channel.unary_unary(
                '/buckets.pb.API/Init',
                request_serializer=buckets__pb2.InitRequest.SerializeToString,
                response_deserializer=buckets__pb2.InitReply.FromString,
                )
        self.Root = channel.unary_unary(
                '/buckets.pb.API/Root',
                request_serializer=buckets__pb2.RootRequest.SerializeToString,
                response_deserializer=buckets__pb2.RootReply.FromString,
                )
        self.Links = channel.unary_unary(
                '/buckets.pb.API/Links',
                request_serializer=buckets__pb2.LinksRequest.SerializeToString,
                response_deserializer=buckets__pb2.LinksReply.FromString,
                )
        self.ListPath = channel.unary_unary(
                '/buckets.pb.API/ListPath',
                request_serializer=buckets__pb2.ListPathRequest.SerializeToString,
                response_deserializer=buckets__pb2.ListPathReply.FromString,
                )
        self.ListIpfsPath = channel.unary_unary(
                '/buckets.pb.API/ListIpfsPath',
                request_serializer=buckets__pb2.ListIpfsPathRequest.SerializeToString,
                response_deserializer=buckets__pb2.ListIpfsPathReply.FromString,
                )
        self.PushPath = channel.stream_stream(
                '/buckets.pb.API/PushPath',
                request_serializer=buckets__pb2.PushPathRequest.SerializeToString,
                response_deserializer=buckets__pb2.PushPathReply.FromString,
                )
        self.PullPath = channel.unary_stream(
                '/buckets.pb.API/PullPath',
                request_serializer=buckets__pb2.PullPathRequest.SerializeToString,
                response_deserializer=buckets__pb2.PullPathReply.FromString,
                )
        self.PullIpfsPath = channel.unary_stream(
                '/buckets.pb.API/PullIpfsPath',
                request_serializer=buckets__pb2.PullIpfsPathRequest.SerializeToString,
                response_deserializer=buckets__pb2.PullIpfsPathReply.FromString,
                )
        self.SetPath = channel.unary_unary(
                '/buckets.pb.API/SetPath',
                request_serializer=buckets__pb2.SetPathRequest.SerializeToString,
                response_deserializer=buckets__pb2.SetPathReply.FromString,
                )
        self.Remove = channel.unary_unary(
                '/buckets.pb.API/Remove',
                request_serializer=buckets__pb2.RemoveRequest.SerializeToString,
                response_deserializer=buckets__pb2.RemoveReply.FromString,
                )
        self.RemovePath = channel.unary_unary(
                '/buckets.pb.API/RemovePath',
                request_serializer=buckets__pb2.RemovePathRequest.SerializeToString,
                response_deserializer=buckets__pb2.RemovePathReply.FromString,
                )
        self.Archive = channel.unary_unary(
                '/buckets.pb.API/Archive',
                request_serializer=buckets__pb2.ArchiveRequest.SerializeToString,
                response_deserializer=buckets__pb2.ArchiveReply.FromString,
                )
        self.ArchiveStatus = channel.unary_unary(
                '/buckets.pb.API/ArchiveStatus',
                request_serializer=buckets__pb2.ArchiveStatusRequest.SerializeToString,
                response_deserializer=buckets__pb2.ArchiveStatusReply.FromString,
                )
        self.ArchiveInfo = channel.unary_unary(
                '/buckets.pb.API/ArchiveInfo',
                request_serializer=buckets__pb2.ArchiveInfoRequest.SerializeToString,
                response_deserializer=buckets__pb2.ArchiveInfoReply.FromString,
                )
        self.ArchiveWatch = channel.unary_stream(
                '/buckets.pb.API/ArchiveWatch',
                request_serializer=buckets__pb2.ArchiveWatchRequest.SerializeToString,
                response_deserializer=buckets__pb2.ArchiveWatchReply.FromString,
                )


class APIServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Root(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Links(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIpfsPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushPath(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullIpfsPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemovePath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Archive(self, request, context):
        """Archive
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArchiveStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArchiveInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ArchiveWatch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_APIServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=buckets__pb2.ListRequest.FromString,
                    response_serializer=buckets__pb2.ListReply.SerializeToString,
            ),
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=buckets__pb2.InitRequest.FromString,
                    response_serializer=buckets__pb2.InitReply.SerializeToString,
            ),
            'Root': grpc.unary_unary_rpc_method_handler(
                    servicer.Root,
                    request_deserializer=buckets__pb2.RootRequest.FromString,
                    response_serializer=buckets__pb2.RootReply.SerializeToString,
            ),
            'Links': grpc.unary_unary_rpc_method_handler(
                    servicer.Links,
                    request_deserializer=buckets__pb2.LinksRequest.FromString,
                    response_serializer=buckets__pb2.LinksReply.SerializeToString,
            ),
            'ListPath': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPath,
                    request_deserializer=buckets__pb2.ListPathRequest.FromString,
                    response_serializer=buckets__pb2.ListPathReply.SerializeToString,
            ),
            'ListIpfsPath': grpc.unary_unary_rpc_method_handler(
                    servicer.ListIpfsPath,
                    request_deserializer=buckets__pb2.ListIpfsPathRequest.FromString,
                    response_serializer=buckets__pb2.ListIpfsPathReply.SerializeToString,
            ),
            'PushPath': grpc.stream_stream_rpc_method_handler(
                    servicer.PushPath,
                    request_deserializer=buckets__pb2.PushPathRequest.FromString,
                    response_serializer=buckets__pb2.PushPathReply.SerializeToString,
            ),
            'PullPath': grpc.unary_stream_rpc_method_handler(
                    servicer.PullPath,
                    request_deserializer=buckets__pb2.PullPathRequest.FromString,
                    response_serializer=buckets__pb2.PullPathReply.SerializeToString,
            ),
            'PullIpfsPath': grpc.unary_stream_rpc_method_handler(
                    servicer.PullIpfsPath,
                    request_deserializer=buckets__pb2.PullIpfsPathRequest.FromString,
                    response_serializer=buckets__pb2.PullIpfsPathReply.SerializeToString,
            ),
            'SetPath': grpc.unary_unary_rpc_method_handler(
                    servicer.SetPath,
                    request_deserializer=buckets__pb2.SetPathRequest.FromString,
                    response_serializer=buckets__pb2.SetPathReply.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=buckets__pb2.RemoveRequest.FromString,
                    response_serializer=buckets__pb2.RemoveReply.SerializeToString,
            ),
            'RemovePath': grpc.unary_unary_rpc_method_handler(
                    servicer.RemovePath,
                    request_deserializer=buckets__pb2.RemovePathRequest.FromString,
                    response_serializer=buckets__pb2.RemovePathReply.SerializeToString,
            ),
            'Archive': grpc.unary_unary_rpc_method_handler(
                    servicer.Archive,
                    request_deserializer=buckets__pb2.ArchiveRequest.FromString,
                    response_serializer=buckets__pb2.ArchiveReply.SerializeToString,
            ),
            'ArchiveStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.ArchiveStatus,
                    request_deserializer=buckets__pb2.ArchiveStatusRequest.FromString,
                    response_serializer=buckets__pb2.ArchiveStatusReply.SerializeToString,
            ),
            'ArchiveInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.ArchiveInfo,
                    request_deserializer=buckets__pb2.ArchiveInfoRequest.FromString,
                    response_serializer=buckets__pb2.ArchiveInfoReply.SerializeToString,
            ),
            'ArchiveWatch': grpc.unary_stream_rpc_method_handler(
                    servicer.ArchiveWatch,
                    request_deserializer=buckets__pb2.ArchiveWatchRequest.FromString,
                    response_serializer=buckets__pb2.ArchiveWatchReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'buckets.pb.API', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class API(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/List',
            buckets__pb2.ListRequest.SerializeToString,
            buckets__pb2.ListReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/Init',
            buckets__pb2.InitRequest.SerializeToString,
            buckets__pb2.InitReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Root(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/Root',
            buckets__pb2.RootRequest.SerializeToString,
            buckets__pb2.RootReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Links(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/Links',
            buckets__pb2.LinksRequest.SerializeToString,
            buckets__pb2.LinksReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/ListPath',
            buckets__pb2.ListPathRequest.SerializeToString,
            buckets__pb2.ListPathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListIpfsPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/ListIpfsPath',
            buckets__pb2.ListIpfsPathRequest.SerializeToString,
            buckets__pb2.ListIpfsPathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PushPath(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/buckets.pb.API/PushPath',
            buckets__pb2.PushPathRequest.SerializeToString,
            buckets__pb2.PushPathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PullPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/buckets.pb.API/PullPath',
            buckets__pb2.PullPathRequest.SerializeToString,
            buckets__pb2.PullPathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PullIpfsPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/buckets.pb.API/PullIpfsPath',
            buckets__pb2.PullIpfsPathRequest.SerializeToString,
            buckets__pb2.PullIpfsPathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/SetPath',
            buckets__pb2.SetPathRequest.SerializeToString,
            buckets__pb2.SetPathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/Remove',
            buckets__pb2.RemoveRequest.SerializeToString,
            buckets__pb2.RemoveReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemovePath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/RemovePath',
            buckets__pb2.RemovePathRequest.SerializeToString,
            buckets__pb2.RemovePathReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Archive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/Archive',
            buckets__pb2.ArchiveRequest.SerializeToString,
            buckets__pb2.ArchiveReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArchiveStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/ArchiveStatus',
            buckets__pb2.ArchiveStatusRequest.SerializeToString,
            buckets__pb2.ArchiveStatusReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArchiveInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/buckets.pb.API/ArchiveInfo',
            buckets__pb2.ArchiveInfoRequest.SerializeToString,
            buckets__pb2.ArchiveInfoReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ArchiveWatch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/buckets.pb.API/ArchiveWatch',
            buckets__pb2.ArchiveWatchRequest.SerializeToString,
            buckets__pb2.ArchiveWatchReply.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
