//////////////////////////////////////////
//
// NOTE: This is *not* a valid shader file
//
///////////////////////////////////////////
Shader "Brave/Internal/GBuffer_LightMaskCombiner" {
Properties {
_MainTex ("Light Mask Base", 2D) = "black" { }
_LightTex ("Light Mask Secondary", 2D) = "black" { }
}
SubShader {
 Pass {
  Blend One OneMinusSrcAlpha, One OneMinusSrcAlpha
  ZTest Always
  GpuProgramID 62812
Program "vp" {
SubProgram "d3d11 " {
"// shader disassembly not supported on DXBC"
}
SubProgram "glcore " {
"#ifdef VERTEX
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 hlslcc_mtx4x4unity_ObjectToWorld[4];
uniform 	vec4 hlslcc_mtx4x4unity_MatrixVP[4];
in  vec4 in_POSITION0;
in  vec2 in_TEXCOORD0;
out vec2 vs_TEXCOORD0;
vec4 u_xlat0;
vec4 u_xlat1;
void main()
{
    u_xlat0 = in_POSITION0.yyyy * hlslcc_mtx4x4unity_ObjectToWorld[1];
    u_xlat0 = hlslcc_mtx4x4unity_ObjectToWorld[0] * in_POSITION0.xxxx + u_xlat0;
    u_xlat0 = hlslcc_mtx4x4unity_ObjectToWorld[2] * in_POSITION0.zzzz + u_xlat0;
    u_xlat0 = u_xlat0 + hlslcc_mtx4x4unity_ObjectToWorld[3];
    u_xlat1 = u_xlat0.yyyy * hlslcc_mtx4x4unity_MatrixVP[1];
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[0] * u_xlat0.xxxx + u_xlat1;
    u_xlat1 = hlslcc_mtx4x4unity_MatrixVP[2] * u_xlat0.zzzz + u_xlat1;
    gl_Position = hlslcc_mtx4x4unity_MatrixVP[3] * u_xlat0.wwww + u_xlat1;
    vs_TEXCOORD0.xy = in_TEXCOORD0.xy;
    return;
}

#endif
#ifdef FRAGMENT
#version 150
#extension GL_ARB_explicit_attrib_location : require
#extension GL_ARB_shader_bit_encoding : enable

uniform 	vec4 _UVRange;
uniform  sampler2D _MainTex;
uniform  sampler2D _LightTex;
in  vec2 vs_TEXCOORD0;
layout(location = 0) out vec4 SV_Target0;
vec2 u_xlat0;
vec4 u_xlat10_0;
vec4 u_xlat10_1;
void main()
{
    u_xlat0.xy = vs_TEXCOORD0.xy * vec2(0.995850623, 0.992647052) + _UVRange.xy;
    u_xlat10_0 = texture(_MainTex, u_xlat0.xy);
    u_xlat10_1 = texture(_LightTex, vs_TEXCOORD0.xy);
    SV_Target0 = max(u_xlat10_0, u_xlat10_1);
    return;
}

#endif
"
}
SubProgram "vulkan " {
"; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 124
; Schema: 0
                                                     OpCapability Shader 
                                              %1 = OpExtInstImport "GLSL.std.450" 
                                                     OpMemoryModel Logical GLSL450 
                                                     OpEntryPoint Vertex %4 "main" %11 %72 %94 %102 
                                                     OpDecorate %11 Location 11 
                                                     OpDecorate %16 ArrayStride 16 
                                                     OpDecorate %17 ArrayStride 17 
                                                     OpMemberDecorate %18 0 Offset 18 
                                                     OpMemberDecorate %18 1 Offset 18 
                                                     OpMemberDecorate %18 2 Offset 18 
                                                     OpDecorate %18 Block 
                                                     OpDecorate %20 DescriptorSet 20 
                                                     OpDecorate %20 Binding 20 
                                                     OpMemberDecorate %70 0 BuiltIn 70 
                                                     OpMemberDecorate %70 1 BuiltIn 70 
                                                     OpMemberDecorate %70 2 BuiltIn 70 
                                                     OpDecorate %70 Block 
                                                     OpDecorate %91 RelaxedPrecision 
                                                     OpDecorate %94 RelaxedPrecision 
                                                     OpDecorate %94 Location 94 
                                                     OpDecorate %97 RelaxedPrecision 
                                                     OpDecorate %98 RelaxedPrecision 
                                                     OpDecorate %100 RelaxedPrecision 
                                                     OpDecorate %102 RelaxedPrecision 
                                                     OpDecorate %102 Location 102 
                                                     OpDecorate %108 RelaxedPrecision 
                                                     OpDecorate %111 RelaxedPrecision 
                                                     OpDecorate %112 RelaxedPrecision 
                                                     OpDecorate %117 RelaxedPrecision 
                                              %2 = OpTypeVoid 
                                              %3 = OpTypeFunction %2 
                                              %6 = OpTypeFloat 32 
                                              %7 = OpTypeVector %6 4 
                                              %8 = OpTypePointer Private %7 
                               Private f32_4* %9 = OpVariable Private 
                                             %10 = OpTypePointer Input %7 
                                Input f32_4* %11 = OpVariable Input 
                                             %14 = OpTypeInt 32 0 
                                         u32 %15 = OpConstant 4 
                                             %16 = OpTypeArray %7 %15 
                                             %17 = OpTypeArray %7 %15 
                                             %18 = OpTypeStruct %16 %17 %7 
                                             %19 = OpTypePointer Uniform %18 
Uniform struct {f32_4[4]; f32_4[4]; f32_4;}* %20 = OpVariable Uniform 
                                             %21 = OpTypeInt 32 1 
                                         i32 %22 = OpConstant 0 
                                         i32 %23 = OpConstant 1 
                                             %24 = OpTypePointer Uniform %7 
                                         i32 %35 = OpConstant 2 
                                         i32 %44 = OpConstant 3 
                              Private f32_4* %48 = OpVariable Private 
                                         u32 %68 = OpConstant 1 
                                             %69 = OpTypeArray %6 %68 
                                             %70 = OpTypeStruct %7 %6 %69 
                                             %71 = OpTypePointer Output %70 
        Output struct {f32_4; f32; f32[1];}* %72 = OpVariable Output 
                                             %80 = OpTypePointer Output %7 
                                             %82 = OpTypeBool 
                                             %83 = OpTypePointer Private %82 
                               Private bool* %84 = OpVariable Private 
                                             %85 = OpTypePointer Uniform %6 
                                         f32 %88 = OpConstant 3.674022E-40 
                                             %90 = OpTypePointer Private %6 
                                Private f32* %91 = OpVariable Private 
                                             %92 = OpTypeVector %6 2 
                                             %93 = OpTypePointer Input %92 
                                Input f32_2* %94 = OpVariable Input 
                                             %95 = OpTypePointer Input %6 
                                         f32 %99 = OpConstant 3.674022E-40 
                                            %101 = OpTypePointer Output %92 
                              Output f32_2* %102 = OpVariable Output 
                                            %103 = OpTypePointer Function %6 
                                            %113 = OpTypePointer Output %6 
                                        u32 %115 = OpConstant 0 
                                         void %4 = OpFunction None %3 
                                              %5 = OpLabel 
                              Function f32* %104 = OpVariable Function 
                                       f32_4 %12 = OpLoad %11 
                                       f32_4 %13 = OpVectorShuffle %12 %12 1 1 1 1 
                              Uniform f32_4* %25 = OpAccessChain %20 %22 %23 
                                       f32_4 %26 = OpLoad %25 
                                       f32_4 %27 = OpFMul %13 %26 
                                                     OpStore %9 %27 
                              Uniform f32_4* %28 = OpAccessChain %20 %22 %22 
                                       f32_4 %29 = OpLoad %28 
                                       f32_4 %30 = OpLoad %11 
                                       f32_4 %31 = OpVectorShuffle %30 %30 0 0 0 0 
                                       f32_4 %32 = OpFMul %29 %31 
                                       f32_4 %33 = OpLoad %9 
                                       f32_4 %34 = OpFAdd %32 %33 
                                                     OpStore %9 %34 
                              Uniform f32_4* %36 = OpAccessChain %20 %22 %35 
                                       f32_4 %37 = OpLoad %36 
                                       f32_4 %38 = OpLoad %11 
                                       f32_4 %39 = OpVectorShuffle %38 %38 2 2 2 2 
                                       f32_4 %40 = OpFMul %37 %39 
                                       f32_4 %41 = OpLoad %9 
                                       f32_4 %42 = OpFAdd %40 %41 
                                                     OpStore %9 %42 
                                       f32_4 %43 = OpLoad %9 
                              Uniform f32_4* %45 = OpAccessChain %20 %22 %44 
                                       f32_4 %46 = OpLoad %45 
                                       f32_4 %47 = OpFAdd %43 %46 
                                                     OpStore %9 %47 
                                       f32_4 %49 = OpLoad %9 
                                       f32_4 %50 = OpVectorShuffle %49 %49 1 1 1 1 
                              Uniform f32_4* %51 = OpAccessChain %20 %23 %23 
                                       f32_4 %52 = OpLoad %51 
                                       f32_4 %53 = OpFMul %50 %52 
                                                     OpStore %48 %53 
                              Uniform f32_4* %54 = OpAccessChain %20 %23 %22 
                                       f32_4 %55 = OpLoad %54 
                                       f32_4 %56 = OpLoad %9 
                                       f32_4 %57 = OpVectorShuffle %56 %56 0 0 0 0 
                                       f32_4 %58 = OpFMul %55 %57 
                                       f32_4 %59 = OpLoad %48 
                                       f32_4 %60 = OpFAdd %58 %59 
                                                     OpStore %48 %60 
                              Uniform f32_4* %61 = OpAccessChain %20 %23 %35 
                                       f32_4 %62 = OpLoad %61 
                                       f32_4 %63 = OpLoad %9 
                                       f32_4 %64 = OpVectorShuffle %63 %63 2 2 2 2 
                                       f32_4 %65 = OpFMul %62 %64 
                                       f32_4 %66 = OpLoad %48 
                                       f32_4 %67 = OpFAdd %65 %66 
                                                     OpStore %48 %67 
                              Uniform f32_4* %73 = OpAccessChain %20 %23 %44 
                                       f32_4 %74 = OpLoad %73 
                                       f32_4 %75 = OpLoad %9 
                                       f32_4 %76 = OpVectorShuffle %75 %75 3 3 3 3 
                                       f32_4 %77 = OpFMul %74 %76 
                                       f32_4 %78 = OpLoad %48 
                                       f32_4 %79 = OpFAdd %77 %78 
                               Output f32_4* %81 = OpAccessChain %72 %22 
                                                     OpStore %81 %79 
                                Uniform f32* %86 = OpAccessChain %20 %35 %68 
                                         f32 %87 = OpLoad %86 
                                        bool %89 = OpFOrdLessThan %87 %88 
                                                     OpStore %84 %89 
                                  Input f32* %96 = OpAccessChain %94 %68 
                                         f32 %97 = OpLoad %96 
                                         f32 %98 = OpFNegate %97 
                                        f32 %100 = OpFAdd %98 %99 
                                                     OpStore %91 %100 
                                       bool %105 = OpLoad %84 
                                                     OpSelectionMerge %107 None 
                                                     OpBranchConditional %105 %106 %109 
                                            %106 = OpLabel 
                                        f32 %108 = OpLoad %91 
                                                     OpStore %104 %108 
                                                     OpBranch %107 
                                            %109 = OpLabel 
                                 Input f32* %110 = OpAccessChain %94 %68 
                                        f32 %111 = OpLoad %110 
                                                     OpStore %104 %111 
                                                     OpBranch %107 
                                            %107 = OpLabel 
                                        f32 %112 = OpLoad %104 
                                Output f32* %114 = OpAccessChain %102 %68 
                                                     OpStore %114 %112 
                                 Input f32* %116 = OpAccessChain %94 %115 
                                        f32 %117 = OpLoad %116 
                                Output f32* %118 = OpAccessChain %102 %115 
                                                     OpStore %118 %117 
                                Output f32* %119 = OpAccessChain %72 %22 %68 
                                        f32 %120 = OpLoad %119 
                                        f32 %121 = OpFNegate %120 
                                Output f32* %122 = OpAccessChain %72 %22 %68 
                                                     OpStore %122 %121 
                                                     OpReturn
                                                     OpFunctionEnd
; SPIR-V
; Version: 1.0
; Generator: Khronos Glslang Reference Front End; 1
; Bound: 48
; Schema: 0
                                                    OpCapability Shader 
                                             %1 = OpExtInstImport "GLSL.std.450" 
                                                    OpMemoryModel Logical GLSL450 
                                                    OpEntryPoint Fragment %4 "main" %11 %43 
                                                    OpExecutionMode %4 OriginUpperLeft 
                                                    OpDecorate %11 RelaxedPrecision 
                                                    OpDecorate %11 Location 11 
                                                    OpDecorate %12 RelaxedPrecision 
                                                    OpDecorate %16 RelaxedPrecision 
                                                    OpMemberDecorate %18 0 Offset 18 
                                                    OpDecorate %18 Block 
                                                    OpDecorate %20 DescriptorSet 20 
                                                    OpDecorate %20 Binding 20 
                                                    OpDecorate %29 RelaxedPrecision 
                                                    OpDecorate %33 RelaxedPrecision 
                                                    OpDecorate %33 DescriptorSet 33 
                                                    OpDecorate %33 Binding 33 
                                                    OpDecorate %34 RelaxedPrecision 
                                                    OpDecorate %37 RelaxedPrecision 
                                                    OpDecorate %38 RelaxedPrecision 
                                                    OpDecorate %38 DescriptorSet 38 
                                                    OpDecorate %38 Binding 38 
                                                    OpDecorate %39 RelaxedPrecision 
                                                    OpDecorate %40 RelaxedPrecision 
                                                    OpDecorate %43 Location 43 
                                                    OpDecorate %44 RelaxedPrecision 
                                                    OpDecorate %45 RelaxedPrecision 
                                                    OpDecorate %46 RelaxedPrecision 
                                             %2 = OpTypeVoid 
                                             %3 = OpTypeFunction %2 
                                             %6 = OpTypeFloat 32 
                                             %7 = OpTypeVector %6 2 
                                             %8 = OpTypePointer Private %7 
                              Private f32_2* %9 = OpVariable Private 
                                            %10 = OpTypePointer Input %7 
                               Input f32_2* %11 = OpVariable Input 
                                        f32 %13 = OpConstant 3.674022E-40 
                                        f32 %14 = OpConstant 3.674022E-40 
                                      f32_2 %15 = OpConstantComposite %13 %14 
                                            %17 = OpTypeVector %6 4 
                                            %18 = OpTypeStruct %17 
                                            %19 = OpTypePointer Uniform %18 
                   Uniform struct {f32_4;}* %20 = OpVariable Uniform 
                                            %21 = OpTypeInt 32 1 
                                        i32 %22 = OpConstant 0 
                                            %23 = OpTypePointer Uniform %17 
                                            %28 = OpTypePointer Private %17 
                             Private f32_4* %29 = OpVariable Private 
                                            %30 = OpTypeImage %6 Dim2D 0 0 0 1 Unknown 
                                            %31 = OpTypeSampledImage %30 
                                            %32 = OpTypePointer UniformConstant %31 
UniformConstant read_only Texture2DSampled* %33 = OpVariable UniformConstant 
                             Private f32_4* %37 = OpVariable Private 
UniformConstant read_only Texture2DSampled* %38 = OpVariable UniformConstant 
                                            %42 = OpTypePointer Output %17 
                              Output f32_4* %43 = OpVariable Output 
                                        void %4 = OpFunction None %3 
                                             %5 = OpLabel 
                                      f32_2 %12 = OpLoad %11 
                                      f32_2 %16 = OpFMul %12 %15 
                             Uniform f32_4* %24 = OpAccessChain %20 %22 
                                      f32_4 %25 = OpLoad %24 
                                      f32_2 %26 = OpVectorShuffle %25 %25 0 1 
                                      f32_2 %27 = OpFAdd %16 %26 
                                                    OpStore %9 %27 
                 read_only Texture2DSampled %34 = OpLoad %33 
                                      f32_2 %35 = OpLoad %9 
                                      f32_4 %36 = OpImageSampleImplicitLod %34 %35 
                                                    OpStore %29 %36 
                 read_only Texture2DSampled %39 = OpLoad %38 
                                      f32_2 %40 = OpLoad %11 
                                      f32_4 %41 = OpImageSampleImplicitLod %39 %40 
                                                    OpStore %37 %41 
                                      f32_4 %44 = OpLoad %29 
                                      f32_4 %45 = OpLoad %37 
                                      f32_4 %46 = OpExtInst %1 40 %44 %45 
                                                    OpStore %43 %46 
                                                    OpReturn
                                                    OpFunctionEnd
"
}
}
Program "fp" {
SubProgram "d3d11 " {
"// shader disassembly not supported on DXBC"
}
SubProgram "glcore " {
""
}
SubProgram "vulkan " {
""
}
}
}
}
Fallback "Diffuse"
}