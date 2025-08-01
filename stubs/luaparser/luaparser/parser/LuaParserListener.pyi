from antlr4 import *
from LuaParser import LuaParser as LuaParser

class LuaParserListener(ParseTreeListener):
    def enterStart_(self, ctx: LuaParser.Start_Context): ...
    def exitStart_(self, ctx: LuaParser.Start_Context): ...
    def enterChunk(self, ctx: LuaParser.ChunkContext): ...
    def exitChunk(self, ctx: LuaParser.ChunkContext): ...
    def enterBlock(self, ctx: LuaParser.BlockContext): ...
    def exitBlock(self, ctx: LuaParser.BlockContext): ...
    def enterStat_empty(self, ctx: LuaParser.Stat_emptyContext): ...
    def exitStat_empty(self, ctx: LuaParser.Stat_emptyContext): ...
    def enterStat_assignment(self, ctx: LuaParser.Stat_assignmentContext): ...
    def exitStat_assignment(self, ctx: LuaParser.Stat_assignmentContext): ...
    def enterStat_functioncall(self, ctx: LuaParser.Stat_functioncallContext): ...
    def exitStat_functioncall(self, ctx: LuaParser.Stat_functioncallContext): ...
    def enterStat_label(self, ctx: LuaParser.Stat_labelContext): ...
    def exitStat_label(self, ctx: LuaParser.Stat_labelContext): ...
    def enterStat_break(self, ctx: LuaParser.Stat_breakContext): ...
    def exitStat_break(self, ctx: LuaParser.Stat_breakContext): ...
    def enterStat_goto(self, ctx: LuaParser.Stat_gotoContext): ...
    def exitStat_goto(self, ctx: LuaParser.Stat_gotoContext): ...
    def enterStat_do(self, ctx: LuaParser.Stat_doContext): ...
    def exitStat_do(self, ctx: LuaParser.Stat_doContext): ...
    def enterStat_while(self, ctx: LuaParser.Stat_whileContext): ...
    def exitStat_while(self, ctx: LuaParser.Stat_whileContext): ...
    def enterStat_repeat(self, ctx: LuaParser.Stat_repeatContext): ...
    def exitStat_repeat(self, ctx: LuaParser.Stat_repeatContext): ...
    def enterStat_if(self, ctx: LuaParser.Stat_ifContext): ...
    def exitStat_if(self, ctx: LuaParser.Stat_ifContext): ...
    def enterStat_for(self, ctx: LuaParser.Stat_forContext): ...
    def exitStat_for(self, ctx: LuaParser.Stat_forContext): ...
    def enterStat_function(self, ctx: LuaParser.Stat_functionContext): ...
    def exitStat_function(self, ctx: LuaParser.Stat_functionContext): ...
    def enterStat_localfunction(self, ctx: LuaParser.Stat_localfunctionContext): ...
    def exitStat_localfunction(self, ctx: LuaParser.Stat_localfunctionContext): ...
    def enterStat_local(self, ctx: LuaParser.Stat_localContext): ...
    def exitStat_local(self, ctx: LuaParser.Stat_localContext): ...
    def enterAttnamelist(self, ctx: LuaParser.AttnamelistContext): ...
    def exitAttnamelist(self, ctx: LuaParser.AttnamelistContext): ...
    def enterNameattrib(self, ctx: LuaParser.NameattribContext): ...
    def exitNameattrib(self, ctx: LuaParser.NameattribContext): ...
    def enterAttrib(self, ctx: LuaParser.AttribContext): ...
    def exitAttrib(self, ctx: LuaParser.AttribContext): ...
    def enterRetstat(self, ctx: LuaParser.RetstatContext): ...
    def exitRetstat(self, ctx: LuaParser.RetstatContext): ...
    def enterLabel(self, ctx: LuaParser.LabelContext): ...
    def exitLabel(self, ctx: LuaParser.LabelContext): ...
    def enterFuncname(self, ctx: LuaParser.FuncnameContext): ...
    def exitFuncname(self, ctx: LuaParser.FuncnameContext): ...
    def enterVarlist(self, ctx: LuaParser.VarlistContext): ...
    def exitVarlist(self, ctx: LuaParser.VarlistContext): ...
    def enterNamelist(self, ctx: LuaParser.NamelistContext): ...
    def exitNamelist(self, ctx: LuaParser.NamelistContext): ...
    def enterExplist(self, ctx: LuaParser.ExplistContext): ...
    def exitExplist(self, ctx: LuaParser.ExplistContext): ...
    def enterExp(self, ctx: LuaParser.ExpContext): ...
    def exitExp(self, ctx: LuaParser.ExpContext): ...
    def enterVar(self, ctx: LuaParser.VarContext): ...
    def exitVar(self, ctx: LuaParser.VarContext): ...
    def enterPrefixexp(self, ctx: LuaParser.PrefixexpContext): ...
    def exitPrefixexp(self, ctx: LuaParser.PrefixexpContext): ...
    def enterFunctioncall_exp(self, ctx: LuaParser.Functioncall_expContext): ...
    def exitFunctioncall_exp(self, ctx: LuaParser.Functioncall_expContext): ...
    def enterFunctioncall_expinvoke(self, ctx: LuaParser.Functioncall_expinvokeContext): ...
    def exitFunctioncall_expinvoke(self, ctx: LuaParser.Functioncall_expinvokeContext): ...
    def enterFunctioncall_invoke(self, ctx: LuaParser.Functioncall_invokeContext): ...
    def exitFunctioncall_invoke(self, ctx: LuaParser.Functioncall_invokeContext): ...
    def enterFunctioncall_nestedinvoke(self, ctx: LuaParser.Functioncall_nestedinvokeContext): ...
    def exitFunctioncall_nestedinvoke(self, ctx: LuaParser.Functioncall_nestedinvokeContext): ...
    def enterFunctioncall_name(self, ctx: LuaParser.Functioncall_nameContext): ...
    def exitFunctioncall_name(self, ctx: LuaParser.Functioncall_nameContext): ...
    def enterFunctioncall_nested(self, ctx: LuaParser.Functioncall_nestedContext): ...
    def exitFunctioncall_nested(self, ctx: LuaParser.Functioncall_nestedContext): ...
    def enterTail(self, ctx: LuaParser.TailContext): ...
    def exitTail(self, ctx: LuaParser.TailContext): ...
    def enterArgs(self, ctx: LuaParser.ArgsContext): ...
    def exitArgs(self, ctx: LuaParser.ArgsContext): ...
    def enterFunctiondef(self, ctx: LuaParser.FunctiondefContext): ...
    def exitFunctiondef(self, ctx: LuaParser.FunctiondefContext): ...
    def enterFuncbody(self, ctx: LuaParser.FuncbodyContext): ...
    def exitFuncbody(self, ctx: LuaParser.FuncbodyContext): ...
    def enterParlist(self, ctx: LuaParser.ParlistContext): ...
    def exitParlist(self, ctx: LuaParser.ParlistContext): ...
    def enterTableconstructor(self, ctx: LuaParser.TableconstructorContext): ...
    def exitTableconstructor(self, ctx: LuaParser.TableconstructorContext): ...
    def enterFieldlist(self, ctx: LuaParser.FieldlistContext): ...
    def exitFieldlist(self, ctx: LuaParser.FieldlistContext): ...
    def enterField(self, ctx: LuaParser.FieldContext): ...
    def exitField(self, ctx: LuaParser.FieldContext): ...
    def enterFieldsep(self, ctx: LuaParser.FieldsepContext): ...
    def exitFieldsep(self, ctx: LuaParser.FieldsepContext): ...
    def enterNumber(self, ctx: LuaParser.NumberContext): ...
    def exitNumber(self, ctx: LuaParser.NumberContext): ...
    def enterString(self, ctx: LuaParser.StringContext): ...
    def exitString(self, ctx: LuaParser.StringContext): ...
